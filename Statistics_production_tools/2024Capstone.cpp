#pragma once
#include "RiotAPIManager.h"

int main() {
    //2분당 최대 100개 쿼리 요청 가능
    // Example summoner name
    string nickname = "SikG"; // Replace with an actual summoner name
    string tag = "KR1";
    string puuid = "Fail";

    // Retrieve summoner information from Riot API
    puuid = get_summoner_puuid_byname(nickname, tag);

    cout << "PUUID: " << puuid;
    return 0;
}
