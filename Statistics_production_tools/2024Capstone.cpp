#pragma once
#include "RiotAPIManager.h"

int main() {
    //2분당 최대 100개 쿼리 요청 가능
   
    ///////////////////////
    // Retrieve summoner information from Riot API_for-test 테스트용
    //puuid = get_summoner_puuid_byname(nickname, tag);
    //cout << "PUUID: " << puuid;
    // Example summoner name
    //string nickname = "SikG"; // Replace with an actual summoner name
    //string tag = "KR1";
    //string puuid = "Fail";
    ////////////////////////

    //유저 리스트 가저오기 테스트
    vector<string> testList = get_user_list_by_tier("DIAMOND", L"Ⅰ");
    for (int i = 0; i < testList.size(); i++) {
		cout << testList[i] << endl;
	}


    //유저 리스트 가저오기 실 구현
    wstring division_list[5] = { L"Ⅰ",  L"Ⅱ",  L"Ⅲ",  L"Ⅳ",  L"Ⅴ" };
    string tier_list[7] = { "IRON", "BRONZE", "SILVER", "GOLD", "PLATINUM", "EMERALD", "DIAMOND"};
    ofstream file("user_list.csv");
    /*if (!file.is_open()) {
        cout << "파일을 열 수 없습니다." << "\n";
    }
    else {
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 5; j++) {
                vector<vector<string>> data = get_user_list_by_tier(tier_list[i], division_list[j]);
                for (int k = 0; k < data.size(); k++) {
                    for (int l = 0; l < data[k].size(); l++) {
						file << data[k][l];
                        if (l != data[k].size() - 1) {
							file << ",";
						}
					}
                    file << "\n";
				}
            }
        }
    }*/
    


    return 0;
}
