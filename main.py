import time
import os

import requests as r


class DiscordNitro:

    def __init__(self) -> None:
        self.dump = []
        self.redeem_url = 'https://discord.com/billing/partner-promotions/1180231712274387115/'
        self.api = 'https://api.discord.gx.games/v1/direct-fulfillment'
        self.partner_id = {"partnerUserId": os.getenv('PARTNER_ID')}  # You need to obtain it on "https://www.opera.com/gx/discord-nitro"
        self.headers = {"authority": "api.discord.gx.games",
                        "content-type": "application/json",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"}

    def __get_discord_token(self) -> str:
        response = r.post(url=self.api, headers=self.headers, json=self.partner_id)
        if response.status_code == 200:
            redeem = self.redeem_url + response.json().get('token')
            return redeem

    def __dump_discord_link(self, urls: str) -> None:
        print(f'Saving URLs...')

        with open('discord_redeem_urls.txt', 'a') as file:
            file.writelines(urls)

        print('URLs dumped successfully')

    def main(self, n_times: int, save: bool) -> None:
        print(f'Generating {n_times} Discord Nitro redeem URLs...')

        for i in range(n_times):
            token = self.__get_discord_token()
            if not token:
                continue
            self.dump.append(token)
            time.sleep(0.2)

        if not save:
            print(self.dump)

        self.__dump_discord_link('\n'.join(self.dump))


if __name__ == '__main__':
    nitro = DiscordNitro()
    nitro.main(2, save=True)
