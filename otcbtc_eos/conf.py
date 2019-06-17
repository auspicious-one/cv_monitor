config = {
    "vc_name": 'BTC',  # ETH,EOS等都可配置,想监控哪个就填哪个（前提是此交易所支持此币种)
    "otc_buy_url": "https://otcbtc.io/sell_offers?currency={0}&fiat_currency=cny&payment_type=all",
    "otc_sell_url": "https://otcbtc.io/buy_offers?currency={0}&fiat_currency=cny&payment_type=all",
    "ding_notice_url": "https://oapi.dingtalk.com/robot/send?access_token=token_id",  # 钉钉群机器人提供的通知url
    "ding_notice_at": ['123****5678'],  # 钉钉要@的用户的手机号
    "max": 70,  # 最大值通知阀值
    "min": 37  # 最小值通知阀值
}
