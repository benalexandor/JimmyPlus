import requests
import json
import pandas as pd

channel_list = list()

channels = [

]

app_store = {
            "tv_plus":
            {
                "type": "Samsung",
                "type2": "\"Samsung\"",
                "url": "https://www.samsung.com/us/appstore/app/G15147002586",
                "url2": "\"https://www.samsung.com/us/appstore/app/G15147002586\""
            },

            "tv_plus_mobile":
            {
                "type": "Google",
                "type2": "\"Google\"",
                "url": "https://play.google.com/store/apps/details?id=com.samsung.android.tvplus",
                "url2": "\"https://play.google.com/store/apps/details?id=com.samsung.android.tvplus\""
            },

            "samsung_free":
            {
                "type": "Samsung",
                "type2": "\"Samsung\"",
                "url": "https://apps.samsung.com/appquery/appDetail.as?appId=com.samsung.android.app.spage",
                "url2": "\"https://apps.samsung.com/appquery/appDetail.as?appId=com.samsung.android.app.spage\""
            },

            "tv_plus_web":
            {
                "type": "Samsung",
                "type2": "\"Samsung\"",
                "url": "https://www.samsungtvplus.com",
                "url2": "\"https://www.samsungtvplus.com\""
            },

            "tv_plus_familyhub":
            {
                "type": "Samsung",
                "type2": "\"Samsung\"",
                "url": "https://www.samsung.com/us/appstore/app/G15147002586",
                "url2": "\"https://www.samsung.com/us/appstore/app/G15147002586\""
            },

            "SCN":
            {
                "type": "Samsung",
                "type2": "\"Samsung\"",
                "url": "https://www.samsung.com/us/appstore/app/G15147002586",
                "url2": "\"https://www.samsung.com/us/appstore/app/G15147002586\""
            }

            }


accounts_meta = {
    "na": {
        "token": "4237953b9ab0f4546f1b14ee8f74cf699b1a8a91cb7eb2bc9f93967426b0c115f0ef610028bb6132426e081af6e126bb2374ceb015af1960e332dc7ba6c527a5945f6558ec42d877452ac437fcf754bc439d44c0b18558fa294330eb8760913464c2ff837e4896fd75c746a215af820f908dddc8279b378199a4a26b8f6804cc",
        "update": {"Active": 2,
                   "HeaderBidderEndpointTimeout": 1850,
                   "HeaderBidderDedup": True,
                   "HeaderBidderDedupAdomain": True,
                   "HeaderBidderDedupCategory": True,
                   "BypassDedupByDurationAsSeparation": 2,
                   "BypassDedupDuration": 30,
                   "BypassIabCatDedup": 2,
                   "HeaderBidderMimeTypes": "video/mp4",
                   "RemoveContentDistribNameFromEndpointRequest": 2,
                   "RemoveContentKeywordsFromEndpointRequest": 2,
                   "RemoveContentNetworkFromEndpointRequest": 2,
                   "RemoveContentSeriesFromEndpointRequest": 2,
                   "RemoveContentTitleFromEndpointRequest": 2
                   }
    },
    "na_scn": {
        "token": "4237953b9ab0f4546f1b14ee8f74cf699b1a8a91cb7eb2bc9f93967426b0c115f0ef610028bb6132426e081af6e126bb2374ceb015af1960e332dc7ba6c527a5945f6558ec42d877452ac437fcf754bc439d44c0b18558fa294330eb8760913464c2ff837e4896fd75c746a215af820f908dddc8279b378199a4a26b8f6804cc",
        "update": {"Active": 2,
                   "HeaderBidderEndpointTimeout": 1000,
                   "HeaderBidderDedup": True,
                   "HeaderBidderDedupAdomain": True,
                   "HeaderBidderDedupCategory": True,
                   "BypassDedupByDurationAsSeparation": 2,
                   "BypassDedupDuration": 30,
                   "BypassIabCatDedup": 2,
                   "HeaderBidderMimeTypes": "video/mp4",
                   "RemoveContentDistribNameFromEndpointRequest": 2,
                   "RemoveContentKeywordsFromEndpointRequest": 2,
                   "RemoveContentNetworkFromEndpointRequest": 2,
                   "RemoveContentSeriesFromEndpointRequest": 2,
                   "RemoveContentTitleFromEndpointRequest": 2
                   }
    },
    "eu": {
        "token": "bd66c6bc1c67e0c82646abcf79b2521bc3a4c41c978c2429268a978602f59a10ecffb9e84678aa079e0dfe0cec3360a70d5558f8ecbb234136227ced5eef23fb8f2514d080cfa1f89eb7af0e6f1a1138daa2c4483791a45d0c1eabe2a674a7dd8d1a5294631fe89396befee13c3ae7300912ffbe838aa55f0682b94eccfe5f00",
        "update": {"Active": 2,
                   "HeaderBidderEndpointTimeout": 1850,
                   "HeaderBidderDedup": True,
                   "HeaderBidderDedupAdomain": True,
                   "HeaderBidderDedupCategory": False,
                   "HeaderBidderGlobalDedup": 2,
                   "HeaderBidderGlobalDedupExpiration": 300,
                   "HeaderBidderMimeTypes": "video/mp4",
                   "RemoveContentDistribNameFromEndpointRequest": 2,
                   "RemoveContentKeywordsFromEndpointRequest": 2,
                   "RemoveContentNetworkFromEndpointRequest": 2,
                   "RemoveContentSeriesFromEndpointRequest": 2,
                   "RemoveContentTitleFromEndpointRequest": 2
                   }
    },
    "eu_scn": {
        "token": "bd66c6bc1c67e0c82646abcf79b2521bc3a4c41c978c2429268a978602f59a10ecffb9e84678aa079e0dfe0cec3360a70d5558f8ecbb234136227ced5eef23fb8f2514d080cfa1f89eb7af0e6f1a1138daa2c4483791a45d0c1eabe2a674a7dd8d1a5294631fe89396befee13c3ae7300912ffbe838aa55f0682b94eccfe5f00",
        "update": {"Active": 2,
                   "HeaderBidderEndpointTimeout": 1000,
                   "HeaderBidderDedup": True,
                   "HeaderBidderDedupAdomain": True,
                   "HeaderBidderDedupCategory": False,
                   "HeaderBidderGlobalDedup": 2,
                   "HeaderBidderGlobalDedupExpiration": 300,
                   "HeaderBidderMimeTypes": "video/mp4",
                   "RemoveContentDistribNameFromEndpointRequest": 2,
                   "RemoveContentKeywordsFromEndpointRequest": 2,
                   "RemoveContentNetworkFromEndpointRequest": 2,
                   "RemoveContentSeriesFromEndpointRequest": 2,
                   "RemoveContentTitleFromEndpointRequest": 2
                   }
    },


    "br": {
        "token": "e23078f39e8bd74cec30c250f6709f93ca9982319d869f664bb86565471f36313449001a3720408a13ee890ece667a9e96a9a369c62d3c4b8ba88599cb130179e9557da25a568d262cac7b439d4facb984353d1a6d919155811ec59027313a84fc9fed1d15cb05b63ff8db0cded567ecab07da772270bae7758c5fe11015eeb8",
        "update": {"Active": 2,
                   "HeaderBidderEndpointTimeout": 1850,
                   "HeaderBidderDedup": True,
                   "HeaderBidderDedupAdomain": False,
                   "HeaderBidderDedupCategory": False,
                   "BypassMediafileDedup": 2,
                   "BypassDedupAdCount": 1,
                   "BypassDedupByAdAsSeparation": 2,
                   "HeaderBidderMimeTypes": "video/mp4",
                   "RemoveContentDistribNameFromEndpointRequest": 2,
                   "RemoveContentKeywordsFromEndpointRequest": 2,
                   "RemoveContentNetworkFromEndpointRequest": 2,
                   "RemoveContentSeriesFromEndpointRequest": 2,
                   "RemoveContentTitleFromEndpointRequest": 2
                   }
    },

    "mx": {
        "token": "f8724e5941aceaf95323fb77c0c3057f3e814878aa385b5d7f62997c84c7074226befce0e90a8d01dbe112f0f7fb69e7342e84a03f14b6e91eabf2e4870b8b0f3491ec30232d2569058326d59ddcae6881d70a890e54196854314e9d03443bf35ba2dbec715bf3f7c4be5f6c1a0a289e5fa8a95cee9c695c98ce2ccd276d5b55",
        "update": {"Active": 2,
                   "HeaderBidderEndpointTimeout": 1850,
                   "HeaderBidderDedup": True,
                   "HeaderBidderDedupAdomain": False,
                   "HeaderBidderDedupCategory": False,
                   "BypassMediafileDedup": 2,
                   "BypassDedupAdCount": 1,
                   "BypassDedupByAdAsSeparation": 2,
                   "HeaderBidderMimeTypes": "video/mp4",
                   "RemoveContentDistribNameFromEndpointRequest": 2,
                   "RemoveContentKeywordsFromEndpointRequest": 2,
                   "RemoveContentNetworkFromEndpointRequest": 2,
                   "RemoveContentSeriesFromEndpointRequest": 2,
                   "RemoveContentTitleFromEndpointRequest": 2
                   }
    },

    "au": {
        "token": "95d1ecb0bd29f71863d3ca0958d5123ae20eeb94420377851133aa4bde60a28b8c1982f0640ddc3c543de80e0ed9a600beb63123f37fb8bf550d7620a6c3c340846cc96d6074ca789f75cf000ef2a979afc83ff219606a25b57660e5bc92d8e593a35a93a876656a9818a15f26ee40794f28c265cdc3104d3c8e912229d8252e",
        "update": {"Active": 2,
                   "HeaderBidderEndpointTimeout": 1850,
                   "BypassAdomainDedup": 2,
                   "BypassDedupAdCount": 2,
                   "BypassDedupByAdAsSeparation": 2,
                   "BypassMediafileDedup": 2,
                   "HeaderBidderDedupAdomain": True,
                   "HeaderBidderMimeTypes": "video/mp4",
                   "RemoveContentDistribNameFromEndpointRequest": 2,
                   "RemoveContentKeywordsFromEndpointRequest": 2,
                   "RemoveContentNetworkFromEndpointRequest": 2,
                   "RemoveContentSeriesFromEndpointRequest": 2,
                   "RemoveContentTitleFromEndpointRequest": 2
                   }
    },

    "in": {
        "token": "f7892ad72232bab842fd5b5cc4e0ff1c047bd25df9ef29fa1172a37031ddabab27848d17d31038e6e12148624ca39e7c3518bb6f39a3710f2f46337a2b410e83af31307d01f50e4a22dd92bc1ee53f4894e12af057c59f660d7b7857cd8fbb6aa5b84dea0ede0208834b814c4c9402d18a31b1b79b7330ae795209485bb2ddc5",
        "update": {"Active": 2,
                   "HeaderBidderEndpointTimeout": 1850,
                   "HeaderBidderDedup": False,
                   "HeaderBidderDedupAdomain": False,
                   "HeaderBidderDedupCategory": False,
                   "HeaderBidderMimeTypes": "video/mp4",
                   "RemoveContentDistribNameFromEndpointRequest": 2,
                   "RemoveContentKeywordsFromEndpointRequest": 2,
                   "RemoveContentNetworkFromEndpointRequest": 2,
                   "RemoveContentSeriesFromEndpointRequest": 2,
                   "RemoveContentTitleFromEndpointRequest": 2
                   }
    },


    "kr": {
        "token": "d90f2b27520871a1818dbc07badc2cb78184019c8ac68cf76ccb2cdcebffdefb8f006b3c62a137cf579a33945fe7552327655c4368a240834bb6d940f2c5ea6206cf350529fbc61b047e99be4d591a76503cd7a9582565d86d24dc23ab4dc7f80483df9bedd5e4626ca11ca1f6dd0ed9e5de984ff663ab73ac15b38cff70346c",
        "update": {"Active": 2,
                   "HeaderBidderEndpointTimeout": 1850,
                   "HeaderBidderDedup": True,
                   "HeaderBidderDedupAdomain": False,
                   "HeaderBidderDedupCategory": False,
                   "HeaderBidderMimeTypes": "video/mp4",
                   "RemoveContentDistribNameFromEndpointRequest": 2,
                   "RemoveContentKeywordsFromEndpointRequest": 2,
                   "RemoveContentNetworkFromEndpointRequest": 2,
                   "RemoveContentSeriesFromEndpointRequest": 2,
                   "RemoveContentTitleFromEndpointRequest": 2
                   }
    }


}


for channel in channels:
    account_name = channel["account"]
    channel_type = channel["type"]
    account_meta = accounts_meta[account_name]

    dynamic_api_url = ("https://api.getpublica.com/v1/public/channel?token=" + account_meta["token"])

    update = account_meta["update"]
    update["name"] = channel["channel_name"]

    # Get channel app store info
    channel_app_store_info = app_store[channel_type]
    channel_app_store_type = channel_app_store_info['type']
    channel_app_store_url= channel_app_store_info['url']

    # Get channel app override info
    channel_app_domain_info = app_store[channel_type]
    channel_app_domain_type = channel_app_store_info['type2']
    channel_app_domain_url = channel_app_store_info['url2']

    # Get Channel appbundle override info

    channel_app_bundle = app_store[channel_type]
    channel_app_bundle_type = channel_app_store_info['type2']
    #app_bundle_override = channel["bundle_override"]


    # Get channel account info
    channel_account_info = accounts_meta[account_name]
    app_store_url = {}
    app_store_url[channel_app_store_type] = channel_app_store_url
    channel_account_info['update']['AppStoreURL'] = app_store_url
    channel_account_info['update']['AppDomainOverride'] = "{" + channel_app_domain_type + ":" + " " + channel_app_domain_url + "}"
    content_rating = channel["rating"]
    channel_account_info['update']['ContentRatingOverride'] = content_rating

    post_bid_channel_name = channel["post_bid_channel_name"]
    channel_account_info['update']["ContentChannelPostBidOverride"] = post_bid_channel_name

    prod_qual_override = channel["Prodqual_Override"]
    channel_account_info['update']["ContentProdqualOverride"] = prod_qual_override

    channel_labels = channel["ChannelLabels"]
    channel_account_info['update']["ChannelLabelNames"] = channel_labels

    response = requests.post(dynamic_api_url, json=update)
    response_dict = response.json()
    channel_info = {
        "id": response_dict["ID"],
        "name": response_dict["name"]
    }
    channel_list.append(channel_info)
    # Print output
    pretty = json.dumps(response_dict, indent=4)
    print(pretty)

pd.DataFrame(channel_list).to_csv(r'/Users/b.alexandor/Desktop/channel_list.csv', index=False)