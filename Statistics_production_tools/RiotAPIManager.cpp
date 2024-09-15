#pragma once
#include "RiotAPIManager.h"
const std::string API_KEY = "RGAPI-a11a32f2-638a-4cd8-9484-07e694aa4d01";
//주기적으로 초기화 해줘야한다

string get_summoner_puuid_byname(const string& name, const string& tag) {
    std::string path = "/riot/account/v1/accounts/by-riot-id/";

    // Build the Riot API request URI
    uri_builder builder(conversions::to_string_t(path));
    builder.append_path(conversions::to_string_t(name));
    builder.append_path(conversions::to_string_t("/" + tag));

    // Include the API key in the query string
    builder.append_query(conversions::to_string_t("api_key"), conversions::to_string_t(API_KEY));

    //// Base URL for the Riot Games API
    http_client client(conversions::to_string_t("https://ASIA.api.riotgames.com"));

    // 동기 요청 수행 및 JSON 응답 처리
    auto resp = client.request(methods::GET, builder.to_string()).get();
    auto json_response = resp.extract_json().get();

    // JSON 응답에서 "puuid" 값을 추출하고 출력
    std::string eid = conversions::to_utf8string(json_response.at(conversions::to_string_t("puuid")).as_string());

    return eid;
}

string get_user_list_by_tier(const string& tier, const string& division) {
    // need to make this class
}

string get_puuid_by_summonerid(const string& puuid) {
    // need to make this class
}

string get_matchlist_by_puuid(const string& puuid) {
    // need to make this class
}

void get_match_by_matchid(const string& matchid) {
    // need to make this class
}

class RiotAPIManager {
    // need to make this class
};