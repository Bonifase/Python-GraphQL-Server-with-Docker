import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return 'Hello ' + name


def main():
    schema = graphene.Schema(query=Query)
    result = schema.execute({'hello'})
    print(result.data['hello'])


if __name__ == '__main__':
    main()
