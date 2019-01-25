from vmconfigtool import (
    config,
    default_git_remote,
)

from vmconfigtool.gui import ansible_win

def main():
    user_config = config.Config()
    user_config.set_value('roles-this-run', [])
    user_config.set_value('git-url', default_git_remote())
    user_config.set_value('git-branch', 'master')
    win = ansible_win.AnsibleWrapperWindow(user_config)
    win.show_all()
    win.main()
    #print("Hello, JMU CS!")


if __name__ == '__main__':
    main()
