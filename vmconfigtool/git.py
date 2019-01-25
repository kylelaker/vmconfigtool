import subprocess

def branch_exists(branch_name):
    """
    Checks whether a particular branch exists at the currently-configured
    git URL. This uses the output of `git ls-remote --heads` and parses the
    branch names from that.
    :param branch_name: The branch name to search for on the remote
    :returns: True if the branch exists and False if it does not
    """

    output = subprocess.run(
        ["/usr/bin/git", "ls-remote", '--heads', USER_CONFIG['git_url']],
        stdout=subprocess.PIPE
    )

    ls_remote = output.stdout.decode("utf-8")

    remote_refs = []
    for ref in ls_remote.split('\n'):
        remote_refs.append(ref.split('/')[-1])

    logging.info("Available branches: %s", ", ".join(remote_refs))

    return branch_name in remote_refs
