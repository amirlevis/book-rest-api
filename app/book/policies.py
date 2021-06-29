from rest_access_policy import AccessPolicy


class BookAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": "*",
            "effect": "allow"
        },
        {
            "action": ["create", "update", "partial_update", "destroy"],
            "principal": ["group:admins"],
            "effect": "allow"
        }
    ]


class AuthorAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": "*",
            "effect": "allow"
        },
        {
            "action": ["create", "update", "partial_update", "destroy"],
            "principal": ["group:admins"],
            "effect": "allow"
        }
    ]


class IllustratorAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["list", "retrieve"],
            "principal": "*",
            "effect": "allow"
        },
        {
            "action": ["create", "update", "partial_update", "destroy"],
            "principal": ["group:admins"],
            "effect": "allow"
        }
    ]
