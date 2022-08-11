# nya translate bot

primitive bot to make translation link between english and chinese channel

## Installation

clone

## Usage

rename the included "config.cfg.example" to "config.cfg", set auth keys and channel_id data.

`"bot_token"` can be obtained from `https://discord.com/developers/applications/{BOT_ID}/bot`

`"deepl_auth_key"` can be obtained from `https://www.deepl.com/pro-account/summary`, the bot assumes you have a free account, despite the URL.

`"channel_en_id"` is the id of the channel where you would expect english speakers to type. NO LONGER USED

`"channel_cn_id"` is the id of the channel where you would expect chinese speakers to type. NO LONGER USED

`"channel_en_ids"` is the list of ids for the channels where you would expect english speakers to type.

`"channel_cn_ids"` is the list of ids for the channels where you would expect chinese speakers to type.

```bash
python translateportal.py
```

## Contributing

please help

## License
[MIT](https://choosealicense.com/licenses/mit/)
