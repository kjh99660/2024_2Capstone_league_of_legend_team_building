### 테이블 정의서
테이블 : matchParticipant
|항목|설명|
|------|---|
|테이블 이름|matchParticipant|
|설명|경기에 참여하는 참가자의 정보를 기록하는 테이블|
|데이터베이스|match5_data_set|

필드 정의
|필드 이름|테이터 타입|null 여부|설명|
|------|----|---|---------|
|numbering|INT(11)|NO|기본 키, 경기 넘버|
|Duration|INT(11)|YES|경기 시간(ms)|
|puuId|VARCHAR(255)|NO|기본 키, 참가자의 암호된 id|
|allInPings|INT(11)|YES| |
|assistMePings|INT(11)|YES| |
|assists|INT(11)|YES| |
|baronKills|INT(11)|YES| |
|basicPings|INT(11)|YES| |
|bountyLevel|INT(11)|YES| |
|champExperience|INT(11)|YES| |
|champLevel|INT(11)|YES| |
|championId|INT(11)|YES| |
|championName|VARCHAR(255)|YES| |
|championTransform|INT(11)|YES| |
|commandPings|INT(11)|YES| |
|consumablesPurchased|INT(11)|YES| |
|damageDealtToBuildings|INT(11)|YES| |
|damageDealtToObjectives|INT(11)|YES| |
|damageDealtToTurrets|INT(11)|YES| |
|damageSelfMitigated|INT(11)|YES| |
|dangerPings|INT(11)|YES| |
|deaths|INT(11)|YES| |
|detectorWardsPlaced|INT(11)|YES| |
|doubleKills|INT(11)|YES| |
|dragonKills|INT(11)|YES| |
|eligibleForProgression|BOOL|YES| |
|enemyMissingPings|INT(11)|YES| |
|enemyVisionPings|INT(11)|YES| |
|firstBloodAssist|BOOL|YES| |
|firstBloodKill|BOOL|YES| |
|firstTowerAssist|BOOL|YES| |
|firstTowerKill|BOOL|YES| |
|gameEndedInEarlySurrender|BOOL|YES| |
|gameEndedInSurrender|BOOL|YES| |
|getBackPings|INT(11)|YES| |
|goldEarned|INT(11)|YES| |
|goldSpent|INT(11)|YES| |
|holdPings|INT(11)|YES| |
|individualPosition|VARCHAR(255)|YES| |
|inhibitorKills|INT(11)|YES| |
|inhibitorTakedowns|INT(11)|YES| |
|inhibitorsLost|INT(11)|YES| |
|item0|INT(11)|YES| |
|item1|INT(11)|YES| |
|item2|INT(11)|YES| |
|item3|INT(11)|YES| |
|item4|INT(11)|YES| |
|item5|INT(11)|YES| |
|item6|INT(11)|YES| |
|itemsPurchased|INT(11)|YES| |
|killingSprees|INT(11)|YES| |
|kills|INT(11)|YES| |
|lane|VARCHAR(255)|YES| |
|largestCriticalStrike|INT(11)|YES| |
|largestKillingSpree|INT(11)|YES| |
|largestMultiKill|INT(11)|YES| |
|longestTimeSpentLiving|INT(11)|YES| |
|magicDamageDealt|INT(11)|YES| |
|magicDamageDealtToChampions|INT(11)|YES| |
|magicDamageTaken|INT(11)|YES| |
|needVisionPings|INT(11)|YES| |
|neutralMinionsKilled|INT(11)|YES| |
|nexusKills|INT(11)|YES| |
|nexusLost|INT(11)|YES| |
|nexusTakedowns|INT(11)|YES| |
|objectivesStolen|INT(11)|YES| |
|objectivesStolenAssists|INT(11)|YES| |
|onMyWayPings|INT(11)|YES| |
|participantId|INT(11)|YES| |
|pentaKills|INT(11)|YES| |
|physicalDamageDealt|INT(11)|YES| |
|physicalDamageDealtToChampions|INT(11)|YES| |
|physicalDamageTaken|INT(11)|YES| |
|placement|INT(11)|YES| |
|playerAugment1|INT(11)|YES| |
|playerAugment2|INT(11)|YES| |
|playerAugment3|INT(11)|YES| |
|playerAugment4|INT(11)|YES| |
|playerAugment5|INT(11)|YES| |
|playerAugment6|INT(11)|YES| |
|playerSubteamId|INT(11)|YES| |
|profileIcon|INT(11)|YES| |
|pushPings|INT(11)|YES| |
|quadraKills|INT(11)|YES| |
|riotIdGameName|VARCHAR(255)|YES| |
|riotIdTagline|VARCHAR(255)|YES| |
|role|VARCHAR(255)|YES| |
|sightWardsBoughtInGame|INT(11)|YES| |
|spell1Casts|INT(11)|YES| |
|spell2Casts|INT(11)|YES| |
|spell3Casts|INT(11)|YES| |
|spell4Casts|INT(11)|YES| |
|subteamPlacement|INT(11)|YES| |
|summoner1Casts|INT(11)|YES| |
|summoner1Id|INT(11)|YES| |
|summoner2Casts|INT(11)|YES| |
|summoner2Id|INT(11)|YES| |
|summonerId|VARCHAR(255)|YES| |
|summonerLevel|INT(11)|YES| |
|summonerName|VARCHAR(255)|YES| |
|teamEarlySurrendered|BOOL|YES| |
|teamId|INT(11)|YES| |
|teamPosition|VARCHAR(255)|YES| |
|timeCCingOthers|INT(11)|YES| |
|timePlayed|INT(11)|YES| |
|totalAllyJungleMinionsKilled|INT(11)|YES| |
|totalDamageDealt|INT(11)|YES| |
|totalDamageDealtToChampions|INT(11)|YES| |
|totalDamageShieldedOnTeammates|INT(11)|YES| |
|totalDamageTaken|INT(11)|YES| |
|totalEnemyJungleMinionsKilled|INT(11)|YES| |
|totalHeal|INT(11)|YES| |
|totalHealsOnTeammates|INT(11)|YES| |
|totalMinionsKilled|INT(11)|YES| |
|totalTimeCCDealt|INT(11)|YES| |
|totalTimeSpentDead|INT(11)|YES| |
|totalUnitsHealed|INT(11)|YES| |
|tripleKills|INT(11)|YES| |
|trueDamageDealt|INT(11)|YES| |
|trueDamageDealtToChampions|INT(11)|YES| |
|trueDamageTaken|INT(11)|YES| |
|turretKills|INT(11)|YES| |
|turretTakedowns|INT(11)|YES| |
|turretsLost|INT(11)|YES| |
|unrealKills|INT(11)|YES| |
|visionClearedPings|INT(11)|YES| |
|visionScore|INT(11)|YES| |
|visionWardsBoughtInGame|INT(11)|YES| |
|wardsKilled|INT(11)|YES| |
|wardsPlaced|INT(11)|YES| |
|win|BOOL|YES| |
|playerScore0|INT(11)|YES| |
|playerScore1|INT(11)|YES| |
|playerScore2|INT(11)|YES| |
|playerScore3|INT(11)|YES| |
|playerScore4|INT(11)|YES| |
|playerScore5|INT(11)|YES| |
|playerScore6|INT(11)|YES| |
|playerScore7|INT(11)|YES| |
|playerScore8|INT(11)|YES| |
|playerScore9|INT(11)|YES| |
|playerScore10|INT(11)|YES| |
|playerScore11|INT(11)|YES| |
|baitPings|INT(11)|YES| |
|riotIdName|VARCHAR(255)|YES| |

제약 조건
|조건 이름|유형|필드 이름|설명|
|------|-----|--------|-------|
|PK_numbering_puuId|Primary Key|numbering, puuId|기본키|

테이블 : challenges
|항목|설명|
|------|---|
|테이블 이름|challenges|
|설명|각 참가자의 challenges 정보를 기록하는 테이블|
|데이터베이스|match5_data_set|

필드 정의
|필드 이름|테이터 타입|null 여부|설명|
|------|----|---|---------|
|numbering|INT(11)|NO|기본 키, 경기 넘버|
|puuId|VARCHAR(255)|NO|기본 키, 참가자의 암호된 id|
|12AssistStreakCount|INT(11)|YES| |
|InfernalScalePickup|INT(11)|YES| |
|SWARM_DefeatAatrox|INT(11)|YES| |
|SWARM_DefeatBriar|INT(11)|YES| |
|SWARM_DefeatMiniBosses|INT(11)|YES| |
|SWARM_EvolveWeapon|INT(11)|YES| |
|SWARM_Have3Passives|INT(11)|YES| |
|SWARM_KillEnemy|INT(11)|YES| |
|SWARM_PickupGold|FLOAT|YES| |
|SWARM_ReachLevel50|INT(11)|YES| |
|SWARM_Survive15Min|INT(11)|YES| |
|SWARM_WinWith5EvolvedWeapons|INT(11)|YES| |
|abilityUses|INT(11)|YES| |
|acesBefore15Minutes|INT(11)|YES| |
|alliedJungleMonsterKills|FLOAT|YES| |
|baronTakedowns|INT(11)|YES| |
|blastConeOppositeOpponentCount|INT(11)|YES| |
|bountyGold|INT(11)|YES| |
|buffsStolen|INT(11)|YES| |
|completeSupportQuestInTime|INT(11)|YES| |
|controlWardTimeCoverageInRiverOrEnemyHalf|FLOAT|YES| |
|controlWardsPlaced|INT(11)|YES| |
|damagePerMinute|FLOAT|YES| |
|damageTakenOnTeamPercentage|FLOAT|YES| |
|dancedWithRiftHerald|INT(11)|YES| |
|deathsByEnemyChamps|INT(11)|YES| |
|dodgeSkillShotsSmallWindow|INT(11)|YES| |
|doubleAces|INT(11)|YES| |
|dragonTakedowns|INT(11)|YES| |
|earlyLaningPhaseGoldExpAdvantage|INT(11)|YES| |
|effectiveHealAndShielding|FLOAT|YES| |
|elderDragonKillsWithOpposingSoul|INT(11)|YES| |
|elderDragonMultikills|INT(11)|YES| |
|enemyChampionImmobilizations|INT(11)|YES| |
|enemyJungleMonsterKills|FLOAT|YES| |
|epicMonsterKillsNearEnemyJungler|INT(11)|YES| |
|epicMonsterKillsWithin30SecondsOfSpawn|INT(11)|YES| |
|epicMonsterSteals|INT(11)|YES| |
|epicMonsterStolenWithoutSmite|INT(11)|YES| |
|firstTurretKilled|INT(11)|YES| |
|fistBumpParticipation|INT(11)|YES| |
|flawlessAces|INT(11)|YES| |
|fullTeamTakedown|INT(11)|YES| |
|gameLength|FLOAT|YES| |
|getTakedownsInAllLanesEarlyJungleAsLaner|INT(11)|YES| |
|goldPerMinute|FLOAT|YES| |
|hadOpenNexus|INT(11)|YES| |
|immobilizeAndKillWithAlly|INT(11)|YES| |
|initialBuffCount|INT(11)|YES| |
|initialCrabCount|INT(11)|YES| |
|jungleCsBefore10Minutes|FLOAT|YES| |
|junglerTakedownsNearDamagedEpicMonster|INT(11)|YES| |
|kTurretsDestroyedBeforePlatesFall|INT(11)|YES| |
|kda|FLOAT|YES| |
|killAfterHiddenWithAlly|INT(11)|YES| |
|killParticipation|FLOAT|YES| |
|killedChampTookFullTeamDamageSurvived|INT(11)|YES| |
|killingSprees|INT(11)|YES| |
|killsNearEnemyTurret|INT(11)|YES| |
|killsOnOtherLanesEarlyJungleAsLaner|INT(11)|YES| |
|killsOnRecentlyHealedByAramPack|INT(11)|YES| |
|killsUnderOwnTurret|INT(11)|YES| |
|killsWithHelpFromEpicMonster|INT(11)|YES| |
|knockEnemyIntoTeamAndKill|INT(11)|YES| |
|landSkillShotsEarlyGame|INT(11)|YES| |
|laneMinionsFirst10Minutes|INT(11)|YES| |
|laningPhaseGoldExpAdvantage|INT(11)|YES| |
|legendaryCount|INT(11)|YES| |
|legendaryItemUsed|VARCHAR(255)|YES| |
|lostAnInhibitor|INT(11)|YES| |
|maxCsAdvantageOnLaneOpponent|FLOAT|YES| |
|maxKillDeficit|INT(11)|YES| |
|maxLevelLeadLaneOpponent|INT(11)|YES| |
|mejaisFullStackInTime|INT(11)|YES| |
|moreEnemyJungleThanOpponent|FLOAT|YES| |
|multiKillOneSpell|INT(11)|YES| |
|multiTurretRiftHeraldCount|INT(11)|YES| |
|multikills|INT(11)|YES| |
|multikillsAfterAggressiveFlash|INT(11)|YES| |
|outerTurretExecutesBefore10Minutes|INT(11)|YES| |
|outnumberedKills|INT(11)|YES| |
|outnumberedNexusKill|INT(11)|YES| |
|perfectDragonSoulsTaken|INT(11)|YES| |
|perfectGame|INT(11)|YES| |
|pickKillWithAlly|INT(11)|YES| |
|playedChampSelectPosition|INT(11)|YES| |
|poroExplosions|INT(11)|YES| |
|quickCleanse|INT(11)|YES| |
|quickFirstTurret|INT(11)|YES| |
|quickSoloKills|INT(11)|YES| |
|riftHeraldTakedowns|INT(11)|YES| |
|saveAllyFromDeath|INT(11)|YES| |
|scuttleCrabKills|INT(11)|YES| |
|skillshotsDodged|INT(11)|YES| |
|skillshotsHit|INT(11)|YES| |
|snowballsHit|INT(11)|YES| |
|soloBaronKills|INT(11)|YES| |
|soloKills|INT(11)|YES| |
|stealthWardsPlaced|INT(11)|YES| |
|survivedSingleDigitHpCount|INT(11)|YES| |
|survivedThreeImmobilizesInFight|INT(11)|YES| |
|takedownOnFirstTurret|INT(11)|YES| |
|takedowns|INT(11)|YES| |
|takedownsAfterGainingLevelAdvantage|INT(11)|YES| |
|takedownsBeforeJungleMinionSpawn|INT(11)|YES| |
|takedownsFirstXMinutes|INT(11)|YES| |
|takedownsInAlcove|INT(11)|YES| |
|takedownsInEnemyFountain|INT(11)|YES| |
|teamBaronKills|INT(11)|YES| |
|teamDamagePercentage|FLOAT|YES| |
|teamElderDragonKills|INT(11)|YES| |
|teamRiftHeraldKills|INT(11)|YES| |
|tookLargeDamageSurvived|INT(11)|YES| |
|turretPlatesTaken|INT(11)|YES| |
|turretTakedowns|INT(11)|YES| |
|turretsTakenWithRiftHerald|INT(11)|YES| |
|twentyMinionsIn3SecondsCount|INT(11)|YES| |
|twoWardsOneSweeperCount|INT(11)|YES| |
|unseenRecalls|INT(11)|YES| |
|visionScoreAdvantageLaneOpponent|FLOAT|YES| |
|visionScorePerMinute|FLOAT|YES| |
|voidMonsterKill|INT(11)|YES| |
|wardTakedowns|INT(11)|YES| |
|wardTakedownsBefore20M|INT(11)|YES| |
|wardsGuarded|INT(11)|YES| |
|junglerKillsEarlyJungle|INT(11)|YES| |
|killsOnLanersEarlyJungleAsJungler|INT(11)|YES| |
|teleportTakedowns|INT(11)|YES| |
|firstTurretKilledTime|FLOAT|YES| |
|shortestTimeToAceFromFirstTakedown|FLOAT|YES| |
|soloTurretsLategame|INT(11)|YES| |
|earliestDragonTakedown|FLOAT|YES| |
|fastestLegendary|FLOAT|YES| |
|highestChampionDamage|INT(11)|YES| |
|highestWardKills|INT(11)|YES| |
|highestCrowdControlScore|INT(11)|YES| |
|fasterSupportQuestCompletion|INT(11)|YES| |
|hadAfkTeammate|INT(11)|YES| |
|earliestBaron|FLOAT|YES| |
|baronBuffGoldAdvantageOverThreshold|INT(11)|YES| |
|thirdInhibitorDestroyedTime|FLOAT|YES| |
|HealFromMapSources|FLOAT|YES| |
|earliestElderDragon|FLOAT|YES| |
|mythicItemUsed|INT(11)|YES| |
|threeWardsOneSweeperCount|INT(11)|YES| |

유의사항 : 
legendaryItemUsed field는 원본 정보가 integer(4자리 item 코드)의 list로 되어 있어
이것을 하나의 string으로 변환하여 저장함(ex. [1022, 2034, 4017] -> "102220344017")

제약 조건
|조건 이름|유형|필드 이름|설명|
|------|-----|--------|-------|
|PK_numbering_puuId|Primary Key|numbering, puuId|기본키|

테이블 : missions
|항목|설명|
|------|---|
|테이블 이름|missions|
|설명|각 참가자의 미션 정보를 기록하는 테이블|
|데이터베이스|match5_data_set|

필드 정의
|필드 이름|테이터 타입|null 여부|설명|
|------|----|---|---------|
|numbering|INT(11)|NO|기본 키, 경기 넘버|
|puuId|VARCHAR(255)|NO|기본 키, 참가자의 암호된 id|
|playerScore0|INT(11)|YES| |
|playerScore1|INT(11)|YES| |
|playerScore2|INT(11)|YES| |
|playerScore3|INT(11)|YES| |
|playerScore4|INT(11)|YES| |
|playerScore5|INT(11)|YES| |
|playerScore6|INT(11)|YES| |
|playerScore7|INT(11)|YES| |
|playerScore8|INT(11)|YES| |
|playerScore9|INT(11)|YES| |
|playerScore10|INT(11)|YES| |
|playerScore11|INT(11)|YES| |

제약 조건
|조건 이름|유형|필드 이름|설명|
|------|-----|--------|-------|
|PK_numbering_puuId|Primary Key|numbering, puuId|기본키|

테이블 : perkStats
|항목|설명|
|------|---|
|테이블 이름|perkStats|
|설명|각 참가자의 퍽 정보를 기록하는 테이블|
|데이터베이스|match5_data_set|

필드 정의
|필드 이름|테이터 타입|null 여부|설명|
|------|----|---|---------|
|numbering|INT(11)|NO|기본 키, 경기 넘버|
|puuId|VARCHAR(255)|NO|기본 키, 참가자의 암호된 id|
|defense|INT(11)|YES| |
|flex|INT(11)|YES| |
|offense|INT(11)|YES| |

제약 조건
|조건 이름|유형|필드 이름|설명|
|------|-----|--------|-------|
|PK_numbering_puuId|Primary Key|numbering, puuId|기본키|

테이블 : perkStyle
|항목|설명|
|------|---|
|테이블 이름|perkStyle|
|설명|각 참가자의 퍽 스타일 정보를 기록하는 테이블|
|데이터베이스|match5_data_set|

필드 정의
|필드 이름|테이터 타입|null 여부|설명|
|------|----|---|---------|
|numbering|INT(11)|NO|기본 키, 경기 넘버|
|puuId|VARCHAR(255)|NO|기본 키, 참가자의 암호된 id|
|primary_style|INT(11)YES| |
|sub_style|INT(11)YES| |
|primary_perk1|INT(11)YES| |
|primary_perk1_value1|INT(11)YES| |
|primary_perk1_value2|INT(11)YES| |
|primary_perk1_value3|INT(11)YES| |
|primary_perk2|INT(11)YES| |
|primary_perk2_value1|INT(11)YES| |
|primary_perk2_value2|INT(11)YES| |
|primary_perk2_value3|INT(11)YES| |
|primary_perk3|INT(11)YES| |
|primary_perk3_value1|INT(11)YES| |
|primary_perk3_value2|INT(11)YES| |
|primary_perk3_value3|INT(11)YES| |
|primary_perk4|INT(11)YES| |
|primary_perk4_value1|INT(11)YES| |
|primary_perk4_value2|INT(11)YES| |
|primary_perk4_value3|INT(11)YES| |
|sub_perk1|INT(11)YES| |
|sub_perk1_value1|INT(11)YES| |
|sub_perk1_value2|INT(11)YES| |
|sub_perk1_value3|INT(11)YES| |
|sub_perk2|INT(11)YES| |
|sub_perk2_value1|INT(11)YES| |
|sub_perk2_value2|INT(11)YES| |
|sub_perk2_value3|INT(11)YES| |

제약 조건
|조건 이름|유형|필드 이름|설명|
|------|-----|--------|-------|
|PK_numbering_puuId|Primary Key|numbering, puuId|기본키|
