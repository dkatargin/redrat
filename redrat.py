#!/usr/bin/python3

import argparse
import configparser
import os
from func import viewer, editor


def parse_args():
    parser = argparse.ArgumentParser(description='RedRat: CLI для работы с RedMine')
    subparsers = parser.add_subparsers()
    parser_view = subparsers.add_parser('view', help='Просмотр задач')
    parser_view.add_argument('view_type', help='list - просмотр в виде списка; num - просмотр количества задач')
    parser_view.add_argument('milestone', help='фильтрация по версиям(all-показать все)')
    parser_view.set_defaults(func=viewer_settings)

    parser_edit = subparsers.add_parser('edit', help='Изменение задач')
    parser_edit.add_argument('edit_type', help='status - смена статуса; comment - добавить комментарий; chown - перевести на userid;')
    parser_edit.add_argument('issue_id', help='номер задачи')
    parser_edit.set_defaults(func=editor_settings)
    return parser.parse_args()


def viewer_settings(args):
    config_path = os.path.join(os.path.dirname(__file__), 'settings.conf')
    config = configparser.ConfigParser()
    config.read(config_path)
    issue_minimal_priority = int(config.get('ReaderSettings', 'MinimalPriority'))
    issue_exclude_projects = tuple(x.strip() for x in config.get('ReaderSettings', 'ExcludeProjects').split(','))
    viewer.ViewIssues(args.view_type, assigned_to='me',
                      minimal_priority=issue_minimal_priority,
                      exclude_projects=issue_exclude_projects, milestone=args.milestone)

def hide_users():
    print(viewer.ViewIssues('users').users)

def editor_settings(args):
    editor.EditIssues(edit_type=args.edit_type, issue_id=args.issue_id)


def main_start():
    args = parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main_start()
    #hide_users()
