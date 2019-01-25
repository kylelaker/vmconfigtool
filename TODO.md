# TODO

This is the list of all the things that need to be done before we can even
consider actually using this as part of the VM.

 - Add logging
 - Get config writing/loading working
 - Implement methods necessary to actually run Ansible
 - Abstract the building of the Ansible command
   - Create a class
   - Add parameters like `url`, `branch`, `tags`, etc.
   - Use this in `vmconfigtool.gui.ansible_win.AnsibleWrapperWindow`
 - Allow `<ENTER>` to save settings
 - Include the JMU-colored Tux icon as part of the project
