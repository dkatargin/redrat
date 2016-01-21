from common.connector import redmine


class EditIssues:
    def __init__(self, edit_type, issue_id):
        self.redmine = redmine()
        self.issue_id = issue_id
        if edit_type == 'status':
            self.change_status()
        elif edit_type == 'chown':
            self.change_owner()
        elif edit_type == 'comment':
            self.add_comment()
        else:
            pass

    def change_status(self):
        selected_issue = self.redmine.issue.get(self.issue_id)
        out_str = '\033[1m%s\033[0m\n%s\nСтатус:\033[4m%s\033[0m\n' % (selected_issue,selected_issue.description,selected_issue.status)
        print(out_str+'='*10)
        print('Выберете новый статус(цифра) задачи:\n')
        for i in self.redmine.issue_status.all():
            print("[%i]\t%s"%(i.id, i))
        new_status = int(input('>> '))
        selected_issue.status_id = new_status
        if selected_issue.save():
            print('Статус задачи изменён')
        else:
            print('Статус задачи не изменён')

    def change_owner(self):
        selected_issue = self.redmine.issue.get(self.issue_id)
        issue_proj = list(filter(lambda p: p.name == selected_issue.project.name, self.redmine.project.all()))
        if not issue_proj:
            return
        issue_proj = issue_proj[0]
        print('На кого перевести задачу(число)?\n')
        for m in issue_proj.memberships:
            print("[%i]\t%s" % (m.id, m.user))
        new_member = int(input('>> '))
        selected_issue.assigned_to_id = new_member
        if selected_issue.save():
            print('Пользователь задачи изменён')
        else:
            print('Пользователь задачи не изменён')

    def add_comment(self):
        pass