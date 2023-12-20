# Discord Nitro Redeem URL Generator

## Disclaimer:
> <b style="color:darkred">I'm not responsible for any illegal/misuse actions, this program was made for educational purposes only.</b>

## Requirements:

- Download OperaGX
- Go to: https://www.opera.com/gx/discord-nitro
- Press <b style="color:yellow">*Ctrl+Shift+C*</b> and go to the <b style="color:yellow">*Network tab*</b>
- Now click on <b style="color:yellow">*Claim now*</b> and look up for <b style="color:yellow">*direct-fullfillment*</b> under the *Network* tab and click on *Payload*
- Then copy the value of <b style="color:yellow">*partnerUserId*</b> and set it as <b style="color:yellow">*PARTNER_ID*</b> on Enviroment Variable.

## How to use it:

- Open the <b style="color:green">*main.py*</b> file
- the <b style="color:green">*main*</b> function receives 2 parameters:
  - n_times (int): the quantity of urls you want to generate
  - save (bool): if you want to dump the URLs you've generated.