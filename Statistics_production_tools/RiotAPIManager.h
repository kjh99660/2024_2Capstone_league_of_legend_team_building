#pragma once
#include <cpprest/http_client.h>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <fstream>

using namespace std;
using namespace utility;                    // Common utilities like string conversions
using namespace web;                        // Common features like URIs.
using namespace web::http;                  // Common HTTP functionality
using namespace web::http::client;          // HTTP client features
using namespace concurrency::streams;       // Asynchronous streams

string get_summoner_puuid_byname(const string& name, const string& tag);
// Function to get the summoner's PUUID by name and tag(for just test API)

vector<string> get_user_list_by_tier(const string& tier, const wstring& division);
// Function to get the list of summoners by tier and division

string get_puuid_by_summonerid(const string& puuid);
// Function to get the summoner's PUUID by summoner ID

string get_matchlist_by_puuid(const string& puuid);
// Function to get the match list by PUUID

void get_match_by_matchid(const string& matchid);
// Function to get the match by match ID
