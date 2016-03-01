from common.connector import redmine
import json


class DataExporter:
    def __init__(self):
        self.redmine = redmine()
        self.users_exporter()
        self.project_exporter()

    def project_exporter(self):
        project_id = 'acme'
        wikies = []
        issues = []
        project = self.redmine.project.get(project_id)
        for w in project.wiki_pages:
            wikies.append({'project_id': project_id,
                           'title': w.title,
                           'text': w.text,
                           'parent_title': '',
                           'comments': w.comments})

        for i in project.issues:
            issues.append({'project_id': project_id,
                           'subject': i.subject,
                           'project': i.project.id,
                           'description': i.description,
                           'priority': i.priority.id,
                           'author': i.author.id,
                           'assigned_to': i.assigned_to.id,
                           'status': i.status.id,
                           'watchers': [n['id'] for n in i.watchers.resources],
                           'start_date': i.start_date.ctime(),
                           'done_ratio': i.done_ratio
                           })
        with open('wiki_%s' % project_id, 'w') as wiki_out:
           json.dump(wikies, wiki_out)

        with open('issue_%s' % project_id, 'w') as issues_out:
           json.dump(issues, issues_out)

    def users_exporter(self):
        user_list = []
        users = self.redmine.user.all(offset=0, limit=250)
        for u in users:
            user_list.append({'login': u.login,
                              'id': u.id,
                              'firstname': u.firstname,
                              'lastname': u.lastname,
                              'mail': u.mail,
                              'password': 'qwerty123',
                              'must_change_passwd': True})
        with open('users', 'w') as users_out:
           json.dump(user_list, users_out)

if __name__ == '__main__':
    DataExporter()