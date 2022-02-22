from functools import reduce

from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import sys

transport = AIOHTTPTransport(url="https://iso-rewards.sundaeswap.finance/query")
client = Client(transport=transport, fetch_schema_from_transport=True)


# Provide a GraphQL query
def get_query(address):
    query_str = ('query rewards {'
                 f'rewards(address: "{address}"){{'
                 'amount epoch reward redeemedAt { unix } } }')
    return gql(query_str)


if __name__ == '__main__':
    result = client.execute(get_query(sys.argv[1]))
    rewardsList = list(map(lambda i: int(i['reward']), result['rewards']))
    totalRewards = reduce(lambda x, y: x + y, rewardsList) / 1000000
    print(f'Your Rewards: {totalRewards} SUNDAE')
