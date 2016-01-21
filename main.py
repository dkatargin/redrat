import configparser
import viewer


def main_start():
    config_path = 'settings.conf'
    config = configparser.ConfigParser()
    config.read(config_path)

    issue_minimal_priority = int(config.get('ReaderSettings', 'MinimalPriority'))
    issue_exclude_projects = tuple(x.strip() for x in config.get('ReaderSettings', 'ExcludeProjects').split(','))
    viewer.ViewIssues('num', assigned_to='me',
                      minimal_priority=issue_minimal_priority,
                      exclude_projects=issue_exclude_projects)


if __name__ == '__main__':
    main_start()