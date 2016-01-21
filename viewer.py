from connector import redmine


class ViewIssues:
    def __init__(self, view_type, assigned_to='me', minimal_priority=0, exclude_projects=()):
        self.redmine = redmine()
        self.assigned_to = assigned_to
        self.minimal_priority = minimal_priority
        self.exclude_projects = exclude_projects
        if view_type == 'list':
            self.filtered_issues()
        else:
            self.num_issues()

    def colorify_priority(self, state):
        if state.id == 2:
            return '\033[92m'
        elif state.id == 4:
            return '\033[1m\033[91m**'
        elif state.id == 3:
            return '\033[91m'
        elif state.id == 1:
            return '\033[94m'
        else:
            return '\033[94m'

    def filtered_issues(self):
        for p in self.redmine.project.all():
            if p.name in self.exclude_projects:
                continue

            issues = self.redmine.issue.filter(project_id=p.identifier, assigned_to_id=self.assigned_to)
            if len(issues) == 0:
                continue

            print('Проект: %s (%s)' % (p.name, p.identifier))
            for i in issues:
                if i.priority.id < self.minimal_priority:
                    continue
                color_priority = self.colorify_priority(i.priority)
                color_state = self.colorify_priority(i.status)
                end_color = '\033[0m'
                print('[%s%s%s][%s%s%s]\t%i:\t%s' %(color_priority,
                                                  i.priority,
                                                  end_color,
                                                  color_state,
                                                  i.status,end_color,
                                                  i.id, i))
            print('='*10)

    def num_issues(self):
        issues = self.redmine.issue.filter(assigned_to_id=self.assigned_to)
        count =  len([i for i in issues if i.priority.id >= self.minimal_priority if i.project.name not in self.exclude_projects])
        print('Активных задач: %i' % count)


class Colorify:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'