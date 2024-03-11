import boto3

iam_client = boto3.client('iam')
print("....",iam_client());

# Get the user name or role ARN (depending on your scenario)
user_name = "Dinkarv"


# List attached policies (ARNs)
attached_policies = iam_client.list_attached_role_policies(RoleName=user_name)["AttachedPolicies"] if ":" in user_name else iam_client.list_attached_user_policies(UserName=user_name)["AttachedPolicies"]

# (Optional) Get inline policy (if applicable)
inline_policy = iam_client.get_user_policy(UserName=user_name) if ":" not in user_name else None

# Print the retrieved information
print("Attached Policies:")
for policy in attached_policies:
    print(f"\t- {policy['PolicyArn']}")

if inline_policy:
    print("Inline Policy:")
    print(inline_policy["PolicyDocument"])
