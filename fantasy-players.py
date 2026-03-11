import csv
import math
import statistics

all_players_25 = []
rb_stats_25 = []
wr_stats_25 = []
qb_stats_25 = []
te_stats_25 = []

#Reading in each file using def
def readfile(file_name):
    data = []
    with open(file_name, newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
        return data

all_players_25 = readfile("FantasyPros_Fantasy_Football_Points_PPR.csv")
all_players_24 = readfile("FantasyPros_Fantasy_Football_Points_PPR (1).csv")
rb_stats_25 = readfile("FantasyPros_Fantasy_Football_Statistics_RB.csv")
wr_stats_25 = readfile("FantasyPros_Fantasy_Football_Statistics_WR.csv")
te_stats_25 = readfile("FantasyPros_Fantasy_Football_Statistics_TE.csv")
qb_stats_25 = readfile("FantasyPros_Fantasy_Football_Statistics_QB.csv")


#Getting rid of random entries that are not players    
all_players_25 = [player for player in all_players_25 if len(player) > 24]
all_players_24 = [player for player in all_players_24 if len(player) > 24]
rb_stats_25 = [player for player in rb_stats_25 if len(player) > 17]
wr_stats_25 = [player for player in wr_stats_25 if len(player) > 16]
qb_stats_25 = [player for player in qb_stats_25 if len(player) > 17]
te_stats_25 = [player for player in te_stats_25 if len(player) > 16]


#creating seperate lists for each position
rb_weekly_25 = []
wr_weekly_25 = []
te_weekly_25 = []
qb_weekly_25 = []
k_weekly_25 = []
def_weekly_25 = []
flex_weekly_25 = []
flex_weekly_24 = []


for player in all_players_25:
    if player[2] == "RB":
        rb_weekly_25.append(player)
    if player[2] == "WR":
        wr_weekly_25.append(player)
    if player[2] == "TE":
        te_weekly_25.append(player)
    if player[2] == "QB":
        qb_weekly_25.append(player)
    if player[2] == "K":
        k_weekly_25.append(player)
    if player[2] == "DST":
        def_weekly_25.append(player)
    if player[2] == "RB" or player[2] == "WR" or player[2] == "TE":
        flex_weekly_25.append(player)

for player in all_players_24:
    if player[2] == "RB" or player[2] == "WR" or player[2] == "TE":
        flex_weekly_24.append(player)

#showing how players ranked in their position by statistic
def stat_rankings(position, positionlist, statistic_num):
    if position == "rb" or position == "qb":
        players = positionlist[1:]
        players.sort(key=lambda player: float(str(player[statistic_num]).replace(",", "")), reverse=True)
        i = 1
        for player in players:
            player[14] = int(player[14])
            if player[14] >= 8:
                player.append(i)
                i += 1
            else:
                player.append(0)
    else:
        players = positionlist[1:]
        players.sort(key=lambda player: float(str(player[statistic_num]).replace(",", "")), reverse=True)
        i = 1
        for player in players:
            player[13] = int(player[13])
            if player[13] >= 10:
                player.append(i)
                i += 1
            else:
                player.append(0)
        

#adding stats to player lists (catch percentage, total yards, total touchdowns, efficiency score)

#RB RATING = EFFICIENCY SCORE + VOLUME SCORE
def safe_float(x):
    try:
        return float(x.replace(",", ""))
    except:
        return 0
for player in rb_stats_25[1:]:
    try:
        c_per = round((float(player[9])/float(player[8]))*100, 1)
    except:
        c_per = 0
    t_yards = int(player[3].replace(",", "")) + int(player[10].replace(",", ""))
    t_td = int(player[7]) + int(player[12])

    try:
        player_rating = round(3* ((2 * safe_float(player[4]) + .65 * safe_float(player[11]) + 110 * (t_td/(safe_float(player[2]) + safe_float(player[9]))) + 0.006 * (safe_float(player[3]) + safe_float(player[10])) + 4 * (t_td/safe_float(player[14])))), 1)
    except:
        player_rating = 0
    if float(player[2]) < 20:
        player_rating = 0
    player.append(c_per)
    player.append(t_yards)
    player.append(t_td)
    player.append(player_rating)

#WR RATING = EFFICIENCY SCORE + volume score
for player in wr_stats_25[1:]:
    try:
        c_per = round((float(player[4])/float(player[2]))*100, 1)
    except:
        c_per = 0
    t_yards = int(player[5].replace(",", "")) + int(player[10].replace(",", ""))
    t_td = int(player[8]) + int(player[11])
    try:
        player_rating = round(1.3 * (1.5 * (safe_float(player[6]) + 0.12 * c_per) + 35 * (t_td/(safe_float(player[9])+safe_float(player[4]))) + 4 * float(player[4])/float(player[13]) + .2 * (safe_float(player[5])+safe_float(player[10]))/float(player[13])), 1)
    except:
        player_rating = 0
    if float(player[2]) < 15:
        player_rating = 0
    player.append(c_per)
    player.append(t_yards)
    player.append(t_td)
    player.append(player_rating)

for player in te_stats_25[1:]:
    try:
        c_per = round((float(player[4])/float(player[2]))*100, 1)
    except:
        c_per = 0
    t_yards = int(player[5].replace(",", "")) + int(player[10].replace(",", ""))
    t_td = int(player[8]) + int(player[11])
    try:
        player_rating = round(1.3 * (1.5 * (safe_float(player[6]) + 0.12 * c_per) + 35 * (t_td/(safe_float(player[9])+safe_float(player[4]))) + 4 * float(player[4])/float(player[13]) + .2 * (safe_float(player[5])+safe_float(player[10]))/float(player[13])), 1)
    except:
        player_rating = 0
    if float(player[2]) < 15:
        player_rating = 0
    player.append(c_per)
    player.append(t_yards)
    player.append(t_td)
    player.append(player_rating)

for player in qb_stats_25[1:]:
    player[5] = int(player[5].replace(",", ""))
    try:
        rush_ypera = round(float(player[11])/float(player[10]), 1)
    except:
        rush_ypera = 0
    t_yards = player[5] + int(player[11].replace(",", ""))
    t_td = int(player[7]) + int(player[12])
    try:
        float(player[3])
        a = 5 * ((float(player[2])/float(player[3]))-0.3)
        b = 0.25 * (float(player[6])-3)
        c = 20 * (float(player[7])/float(player[3]))
        d = 2.375 - ((float(player[8])/float(player[3])) * 25)
        if a < 0:
            a = 0
        elif a > 2.375:
            a = 2.375
        if b < 0:
            b = 0
        elif b > 2.375:
            b = 2.375
        if c < 0:
            c = 0
        elif c > 2.375:
            c = 2.375
        if d < 0:
            d = 0
        elif d > 2.375:
            d = 2.375
        passer_rating = round(100 * ((a + b + c + d)/6), 1)
    except:
        passer_rating = 0
    player.append(rush_ypera)
    player.append(t_yards)
    player.append(t_td)
    player.append(passer_rating)



#ranking players in lists by the index of the statistic
stat_rankings("rb", rb_stats_25, 2)
stat_rankings("rb", rb_stats_25, 3)
stat_rankings("rb", rb_stats_25, 4)
stat_rankings("rb", rb_stats_25, 7)
stat_rankings("rb", rb_stats_25, 8)
stat_rankings("rb", rb_stats_25, 9)
stat_rankings("rb", rb_stats_25, 10)
stat_rankings("rb", rb_stats_25, 12)
stat_rankings("rb", rb_stats_25, 19)
stat_rankings("rb", rb_stats_25, 20)
stat_rankings("rb", rb_stats_25, 16)
stat_rankings("rb", rb_stats_25, 21)

stat_rankings("wr", wr_stats_25, 2)
stat_rankings("wr", wr_stats_25, 4)
stat_rankings("wr", wr_stats_25, 17)
stat_rankings("wr", wr_stats_25, 5)
stat_rankings("wr", wr_stats_25, 6)
stat_rankings("wr", wr_stats_25, 8)
stat_rankings("wr", wr_stats_25, 18)
stat_rankings("wr", wr_stats_25, 19)
stat_rankings("wr", wr_stats_25, 15)
stat_rankings("wr", wr_stats_25, 20)

stat_rankings("te", te_stats_25, 2)
stat_rankings("te", te_stats_25, 4)
stat_rankings("te", te_stats_25, 17)
stat_rankings("te", te_stats_25, 5)
stat_rankings("te", te_stats_25, 6)
stat_rankings("te", te_stats_25, 8)
stat_rankings("te", te_stats_25, 18)
stat_rankings("te", te_stats_25, 19)
stat_rankings("te", te_stats_25, 15)
stat_rankings("te", te_stats_25, 20)

stat_rankings("qb", qb_stats_25, 2)
stat_rankings("qb", qb_stats_25, 3)
stat_rankings("qb", qb_stats_25, 4)
stat_rankings("qb", qb_stats_25, 5)
stat_rankings("qb", qb_stats_25, 6)
stat_rankings("qb", qb_stats_25, 7)
stat_rankings("qb", qb_stats_25, 8)
stat_rankings("qb", qb_stats_25, 10)
stat_rankings("qb", qb_stats_25, 11)
stat_rankings("qb", qb_stats_25, 18)
stat_rankings("qb", qb_stats_25, 12)
stat_rankings("qb", qb_stats_25, 19)
stat_rankings("qb", qb_stats_25, 20)
stat_rankings("qb", qb_stats_25, 16)
stat_rankings("qb", qb_stats_25, 21)

#function for sorting by a statistic

def sorting(plist, index):
    players = plist[1:]
    players.sort(key=lambda player: float(str(player[index]).replace(",", "")), reverse=True)
    for player in players[:15]:
        print(player[1], "   ", player[index])
    
while True:
    path = input("What would you like to do?\nPlayer analysis (a)\nPositional statistics (s)\n").lower()
    if path == 'a': 

#specific player statistics:

        pl_choice = input("Choose a player to view, or quit(Q): ")
        
        if pl_choice == "Q" or pl_choice == "q":
            break
        else:
            pos = None
            for player in all_players_25:
                if player[1].lower() == pl_choice.lower():
                     pos = player[2]
                    
        if pos == "RB":
            for player in rb_stats_25:
                if player[1].lower().startswith(pl_choice.lower()):
                    print(f"\n\nName: {pl_choice}\nRank: {player[0]}")
                    print(f"\nRush Attempts: {player[2]}  ({player[22]})\nRush Yards: {player[3]}  ({player[23]})\nRush Y/A: {player[4]}  ({player[24]})\nRushing Touchdowns: {player[7]}  ({player[25]})")
                    print(f"\nTargets: {player[8]}  ({player[26]})\nReceptions: {player[9]}  ({player[27]})\nCatch Percentage: {player[18]}%\nRecieving Yards: {player[10]}  ({player[28]})")
                    print(f"Yards Per Catch: {player[11]}\nRecieving Touchdowns: {player[12]}  ({player[29]})")
                    print(f"\nGames Played: {player[14]}\nTotal Yards: {player[19]}  ({player[30]})\nTotal Touchdowns: {player[20]}  ({player[31]})\nTotal Fantasy points: {player[15]}\nFantasy PPG: {player[16]}  ({player[32]})\nPlayer efficiency rating: {player[21]}  ({player[33]})\n\n")
                    print("\n")
        if pos == "WR":
            for player in wr_stats_25:
                if player[1].lower().startswith(pl_choice.lower()):
                    print(f"\n\nName: {pl_choice}\nRank: {player[0]}")
                    print(f"\nRush Attempts: {player[9]}\nRush Yards: {player[10]}\nRushing Touchdowns: {player[11]}")
                    print(f"\nTargets: {player[2]}  ({player[21]})\nReceptions: {player[4]}  ({player[22]})\nCatch Percentage: {player[17]}%  ({player[23]})\nRecieving Yards: {player[5]}  ({player[24]})")
                    print(f"Yards Per Catch: {player[6]}  ({player[25]})\nRecieving Touchdowns: {player[8]}  ({player[26]})")
                    print(f"\nGames Played: {player[13]}\nTotal Yards: {player[18]}  ({player[27]})\nTotal Touchdowns: {player[19]}  ({player[28]})\nTotal Fantasy points: {player[14]}\nFantasy PPG: {player[15]}  ({player[29]})\nPlayer efficiency rating: {player[20]}  ({player[30]})\n\n")
                    print("\n")
        if pos == "TE":
            for player in te_stats_25:
                if player[1].lower().startswith(pl_choice.lower()):
                    print(f"\n\nName: {pl_choice}\nRank: {player[0]}")
                    print(f"\nRush Attempts: {player[9]}\nRush Yards: {player[10]}\nRushing Touchdowns: {player[11]}")
                    print(f"\nTargets: {player[2]}  ({player[21]})\nReceptions: {player[4]}  ({player[22]})\nCatch Percentage: {player[17]}%  ({player[23]})\nRecieving Yards: {player[5]}  ({player[24]})")
                    print(f"Yards Per Catch: {player[6]}  ({player[25]})\nRecieving Touchdowns: {player[8]}  ({player[26]})")
                    print(f"\nGames Played: {player[13]}\nTotal Yards: {player[18]}  ({player[27]})\nTotal Touchdowns: {player[19]}  ({player[28]})\nTotal Fantasy points: {player[14]}\nFantasy PPG: {player[15]}  ({player[29]})\nPlayer efficiency rating: {player[20]}  ({player[30]})\n\n")
                    print("\n")
        if pos == "QB":
            for player in qb_stats_25:
                if player[1].lower().startswith(pl_choice.lower()):
                    print(f"\n\nName: {pl_choice}\nRank: {player[0]}")
                    print(f"\nCompletions: {player[2]}  ({player[22]})\nAttempts: {player[3]}  ({player[23]})\nCompletion Percentage: {player[4]}%  ({player[24]})")
                    print(f"Passing Yards: {player[5]}  ({player[25]})\nYards Per Attempt: {player[6]}  ({player[26]})\nPassing Touchdowns: {player[7]}  ({player[27]})\nInterceptions: {player[8]}  ({player[28]})")
                    print(f"\nRushing Attempts: {player[10]}  ({player[29]})\nRushing Yards: {player[11]}  ({player[30]})\nRushing Yards Per Attempt: {player[18]}  ({player[31]})\nRushing Touchdowns: {player[12]}  ({player[32]})")
                    print(f"\nGames Played: {player[14]}\nTotal Yards: {player[19]}  ({player[33]})\nTotal Touchdowns: {player[20]}  ({player[34]})\nTotal Fantasy points: {player[15]}\nFantasy PPG: {player[16]}  ({player[35]})\nPasser Rating: {player[21]}  ({player[36]})\n\n")
                    print("\n")

        if pos == None:
            print("\n\nInvalid Input\n\n")




#RB/WR weekly std dev
            
    if path == 's':
        stat_path = input("\nWhat statistic would you like to calculate?\nWeekly standard deviation (d)\nBreakout players (b)\nSort by statistic (s)\n").lower()
        if stat_path == "d":
            print("What range of players would you like to test?")
            pl_count1 = input("Lower range: ")
            pl_count2 = input("Higher range: ")
            try:
                pl_count1 = int(pl_count1)
                pl_count2 = int(pl_count2)
                if pl_count1 < 0 or pl_count1 >= pl_count2 or pl_count2 > 200:
                    print("\nHigher range must be higher than lower range, lower range must be greater than 0, higher range must be lower than 200. Try again.\n")
                    continue
            except ValueError:
                print("Invalid input, must be an integer.")
                continue
            tot_pl = 0
            avg_dev = 0
            for player in rb_weekly_25[pl_count1:pl_count2]:
                weekly_dev = []
                for i in range(5, 23):
                    try:
                        player[i] = float(player[i])
                        weekly_dev.append(player[i])
                    except:
                        continue
                if len(weekly_dev) < 2:
                    continue
                tot_pl += 1
                pl_dev = statistics.pstdev(weekly_dev)
                avg_dev += pl_dev
            avg_std_dev = round(avg_dev/tot_pl, 2)
            print(f"\n\nThe RBs ranked between {pl_count1}, and {pl_count2} have an average weekly standard deviation of: ", avg_std_dev)

            tot_pl = 0
            avg_dev = 0
            for player in wr_weekly_25[pl_count1:pl_count2]:
                weekly_dev = []
                for i in range(5, 23):
                    try:
                        player[i] = float(player[i])
                        weekly_dev.append(player[i])
                    except:
                        continue
                if len(weekly_dev) < 2:
                    continue
                tot_pl += 1
                pl_dev = statistics.pstdev(weekly_dev)
                avg_dev += pl_dev
            avg_std_dev = round(avg_dev/tot_pl, 2)
            print(f"The WRs ranked between {pl_count1}, and {pl_count2} have an average weekly standard deviation of: ", avg_std_dev, "\n\n")

#Measuring breakout potential using end of season statistics
        
        if stat_path == "b":
            flex_bo = []
            for player in flex_weekly_25[1:]:
                total_end = 0
                games = 0
                for i in range(18, 23):
                    if float(player[23]) > 0:
                        try:
                            total_end += float(player[i])
                            games += 1
                        except:
                            continue
                if games > 3 and float(player[23]) > 6:
                    average_end = round(total_end/games, 2)
                    bo_rating = round(average_end/(float(player[23])), 2)
                    flex_bo.append([player[1], player[2], player[23], average_end, bo_rating])
                    flex_bo.sort(key=lambda x: x[4], reverse=True)
            for i in range(30):
                print(flex_bo[i])

#Sorting by statistic

        if stat_path == "s":
            pos_stat = input("Choose a stat to sort by:\n\nRunning Backs:\nRushing Yards (a), Yards Per Carry (b), Rushing touchdowns (c), Total yards (d), Total Touchdowns (e), Rating (f)\n\nRecievers:\nRecieving yards (g), Receptions (h), Yards per perception (i), Catch Percentage(j) recieving touchdowns (k), Rating (l)\n\nQuarterbacks:\nPassing yards (m), Yards per attempt (n), Completion percentage (o), Passer rating(p)\n\nChoose an option: ").lower()
            if pos_stat == "a":
                sorting(rb_stats_25, 3)
            elif pos_stat == "b":
                sorting(rb_stats_25, 4)
            elif pos_stat == "c":
                sorting(rb_stats_25, 7)
            elif pos_stat == "d":
                sorting(rb_stats_25, 19)
            elif pos_stat == "e":
                sorting(rb_stats_25, 20)
            elif pos_stat == "f":
                sorting(rb_stats_25, 21)
            elif pos_stat == "g":
                sorting(wr_stats_25, 5)
            elif pos_stat == "h":
                sorting(wr_stats_25, 4)
            elif pos_stat == "i":
                sorting(wr_stats_25, 6)
            elif pos_stat == "j":
                sorting(wr_stats_25, 17)
            elif pos_stat == "k":
                sorting(wr_stats_25, 8)
            elif pos_stat == "l":
                sorting(wr_stats_25, 20)
            elif pos_stat == "m":
                sorting(qb_stats_25, 5)
            elif pos_stat == "n":
                sorting(qb_stats_25, 6)
            elif pos_stat == "o":
                sorting(qb_stats_25, 4)
            elif pos_stat == "p":
                sorting(qb_stats_25, 21)
            
            


            
