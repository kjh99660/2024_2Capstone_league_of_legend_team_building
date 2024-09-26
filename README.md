# 2024_2Capstone_league_of_legend_team_building
## 
## 중앙대학교 2024-2학기 캡스톤 프로젝트  
리그오브레전드 사전구성 5인 팀빌딩 추천 시스템  


###  고려 사항
1. 초당 20회 2분당 100회로 API 호출 횟수 제한 사항이 있다


### 개발 일지  
2024.09.15 RIOT API 체크를 통해 정보 수집 과정 간략하게 정리
2024.09.26 현재 1~4번 코드 개발 및 1~3 자료 추출 완료  



### 자료 추출 과정 요약  
1. 티어입력과정 아이언1~다이아1까지 각각 100개씩 약 2800개의 계정의 summonerID 목록을 만든다 쿼리 28번 > 3분 소요  
Ex. https://kr.api.riotgames.com/lol/league/v4/entries/RANKED_FLEX_SR/DIAMOND/I?page=1  

2. 각 summonerID로 puuid를 알아낸다 > 쿼리 2800번 1시간 소요  
Ex. "https://kr.api.riotgames.com/lol/summoner/v4/summoners/" + summonerID  

3. puuid로 최근 매치id 20개를 받아온다 > 전체 약 20 x 2800 = 56000 경기를 받아온다 > 쿼리 2800번 1시간 소요  
Ex. "https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?start=0&count=20"  

4. 각 경기에서 2 * 5C2 = 20 조합의 승률을 기록한다 > 승률 개수 20x56000 = 1120000 110만개의 승패 정보 저장 > 쿼리 56000번 > 19시간 소요  
각 경기에서 경기 길이 및 각 플레이어 (10명)의 정보를 csv 파일로 저장한다
참조 : op.gg가 700만개 정도 표본확보함  
Ex. "https://asia.api.riotgames.com/lol/match/v5/matches/" + matchid  

### 자료 가공 과정 요약  
예정

