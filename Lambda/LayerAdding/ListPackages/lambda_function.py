import pkg_resources

def lambda_handler(event, context):
    pkgs = pkg_resources.working_set
    pkgs_list = sorted([f'{i.key}=={i.version}' for i in pkgs])
    print("\n".join(pkgs_list))