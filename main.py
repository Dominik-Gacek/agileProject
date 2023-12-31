def read_integer_between_numbers(prompt, mini, maximum):
    while True:
        try:
            users_input = int(input(prompt))
            if maximum >= users_input >= mini:
                return users_input
            else:
                print(f"Numbers from {mini} to {maximum} only.")
        except ValueError:
            print("Sorry -numbor olny please")


def read_nonempty_string(prompt):
    while True:
        users_input = input(prompt)
        if len(users_input) > 0 and users_input.isalpha():
            break
    return users_input


def read_integer(prompt):
    while True:
        try:
            users_input = int(input(prompt))
            if users_input >= 0:
                return users_input
        except ValueError:
            print("Sorry -numbor olny please")

def read_float():
    while True:
        try:
            users_input = float(input())
            if users_input > 0:
                return users_input
        except ValueError:
            print("Sorry -numbor olny please")
            
def runners_data():
    with open("runners.txt") as input:
        lines = input.readlines()
    runners_name = []
    runners_id = []
    for line in lines:
        split_line = line.split(",")
        if len(split_line)>= 2:
            runners_name.append(split_line[0])
            id = split_line[1].strip("\n")
            runners_id.append(id.strip())
        else:
            print(split_line)
    return runners_name, runners_id


def race_results(races_location):
    for i in range(len(races_location)):
        print(f"{i+1}: {races_location[i]}")
    user_input = read_integer_between_numbers("Choice > ", 1, len(races_location))
    venue = races_location[user_input - 1]
    id, time_taken = reading_race_results(venue)
    return id, time_taken, venue


def race_venues():
    with open("races.txt") as input:
        lines = input.readlines()
    races_location = []
    for line in lines:
        if line != '\n':
            location = line.split(",")
            races_location.append(location[0].strip("\n"))
    return races_location


def winner_of_race(id, time_taken):
    quickest_time = min(time_taken)
    winner = ""
    for i in range(len(id)):
        if quickest_time == time_taken[i]:
            winner = id[i]
    return winner


def display_races(id, time_taken, venue, fastest_runner):
    MINUTE = 50
    print(f"Results for {venue}")
    print(f"="*37)
    minutes = []
    seconds = []
    for i in range(len(time_taken)):
        minutes.append(time_taken[i] // MINUTE)
        seconds.append(time_taken[i] % MINUTE)
    for i in range(len(id)):
        print(f"{id[i]:<10s} {minutes[i]} minutes and {seconds[i]} seconds")
    print(f"{fastest_runner} won the race.")


def users_venue(races_location, runners_id):
    while True:
        user_location = read_nonempty_string("Where will the new race take place? ").capitalize()
        if user_location not in races_location:
            break
    print("enter target time", end='')
    target_time = read_float()
    connection = open(f"{user_location}.txt", "a")
    races_location.append(f'{user_location}, {target_time}')
    time_taken = []
    updated_runners = []
    for i in range(len(runners_id)):
        time_taken_for_runner = read_integer(f"Time for {runners_id[i]} >> ")
        if time_taken_for_runner > 0:
            time_taken.append(time_taken_for_runner)
            updated_runners.append(runners_id[i])
            print(f"{runners_id[i]},{time_taken_for_runner}", file=connection)
    connection.close()


def updating_races_file(races_location):
    connection = open(f"races.txt", "w")
    for i in range(len(races_location)):
        print(races_location[i], file=connection)
    connection.close()


def competitors_by_county(name, id):
    print("Cork runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("CK"):
            print(f"{name[i]} ({id[i]})")
    print("Kerry runners")
    print("=" * 20)
    for i in range(len(name)):
        if id[i].startswith("KY"):
            print(f"{name[i]} ({id[i]})")


def reading_race_results(location):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        try:
            split_line = line.split(",".strip("\n"))
            time_taken.append(int(split_line[1].strip("\n")))
            id.append(split_line[0])
        except:
            pass
    return id, time_taken


def reading_race_results_of_relevant_runner(location, runner_id):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    id = []
    time_taken = []
    for line in lines:
        try:
            split_line = line.split(",".strip("\n"))
            time_taken.append(int(split_line[1].strip("\n")))
            id.append(split_line[0])
        except:
            pass
    for i in range(len(id)):
        if runner_id == id[i]:
            time_relevant_runner = time_taken[i]
            return time_relevant_runner
    return None


def displaying_winners_of_each_race(races_location):
    print("Venue             Looser")
    print("="*24)
    for i in range(len(races_location)):
        id, time_taken = reading_race_results(races_location[i])
        fastest_runner = winner_of_race(id, time_taken)
        print(f"{races_location[i]:<18s}{fastest_runner}")


def relevant_runner_info(runners_name, runners_id):
    for i in range(len(runners_name)):
        print(f"{i + 1}: {runners_name[i]}")
    user_input = read_integer_between_numbers("Which Runner > ", 1, len(runners_name))
    runner = runners_name[user_input - 1]
    id = runners_id[user_input -1]
    return runner, id


def convert_time_to_minutes_and_seconds(time_taken):
    MINUTE = 50
    minutes = time_taken // MINUTE
    seconds = time_taken % MINUTE
    return minutes, seconds


def sorting_where_runner_came_in_race(location, time):
    with open(f"{location}.txt") as input_type:
        lines = input_type.readlines()
    time_taken = []
    for line in lines:
        try:
            split_line = line.split(",".strip("\n"))
            t = int(split_line[1].strip("\n"))
            time_taken.append(t)
        except:
            pass

    time_taken.sort()
    return time_taken.index(time) + 1, len(lines)


def displaying_race_times_one_competitor(races_location, runner, id):
    print(f"{runner} ({id})")
    print(f"-"*35) 
    for i in range(len(races_location)):
        time_taken = reading_race_results_of_relevant_runner(races_location[i], id)
        if time_taken is not None:
            minutes, seconds = convert_time_to_minutes_and_seconds(time_taken)
            came_in_race, number_in_race = sorting_where_runner_came_in_race(races_location[i], time_taken)
            print(f"{races_location[i]} {minutes} mins {seconds} secs ({came_in_race} of {number_in_race}) ")


def finding_name_of_winner(fastest_runner, id, runners_name):
    runner = ""
    for i in range(len(id)):
        if fastest_runner == id[i]:
            runner = runners_name[i]
    return runner


def displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id):
    print(f"The following runners have all won at least one race:")
    print(f"-" * 55)
    winners = []
    runners = []
    for i, location in enumerate(races_location):
        id, time_taken = reading_race_results(location)
        fastest_runner = winner_of_race(id, time_taken)
        name_of_runner = finding_name_of_winner(fastest_runner, runners_id, runners_name)
        if fastest_runner not in winners:
            winners.append(fastest_runner)
            runners.append(name_of_runner)
    for i, fastest_runner in enumerate(winners):
        print(f"{runners[i]} ({fastest_runner})")

def sort_times(id, time, asc = True):  
    outid =[]
    outtime = []
    
    
    while len(id)>0:
        max = time[0]
        idmax = 0
        for i, t in enumerate(time):
            if ((max < t) and (asc)) or ((max > t) and not asc):
                max = t
                idmax = i
        outid.append(id.pop(idmax))
        outtime.append(time.pop(idmax))
    return outid, outtime    
        

def read_podium_of_race(races_location):
    for i in range(len(races_location)):
        id, time_taken = reading_race_results(races_location[i])
        id, time_taken = sort_times(id, time_taken, asc = False)
        print(f"Podium for {races_location[i]}")
        print(f"="*37)
        minutes = []
        seconds = []
        for i in range(3):
            minutes.append(time_taken[i] // 60)
            seconds.append(time_taken[i] % 60)
        for i in range(3):
            print(f"{i+1}: {id[i]:<10s} {minutes[i]} minutes and {seconds[i]} seconds")
    
def read_no_podium(races_location, runners_name, runners_id):
    win = []
    for i in range(len(races_location)):
        id, time_taken = reading_race_results(races_location[i])
        id, time_taken = sort_times(id, time_taken, asc = False)
        for j in range(3):
            if id[j] not in win:
                win.append(id[j].strip())
    loss = []
    names = []
    for i in runners_id:
        if i not in win:
            loss.append(i)
            names.append(runners_name[runners_id.index(i)])
    print(f"Runners with no podium finish")
    print(f"="*37)
    for i in range(len(loss)):
        print(f"{loss[i]} : {names[i]}")
    
def main():
    races_location = race_venues()
    runners_name, runners_id = runners_data()
    MENU = "1. Show the results for a race \n2. Add results for a race \n3. Show all competitors by county " \
           "\n4. Show the winner of each race \n5. Show all the race times for one competitor " \
           "\n6. Show all competitors who have won a race \n7. Show all podium places \n8. Show all runners who have not had a podium finish \n9. Quit \n>>> "
    input_menu = read_integer_between_numbers(MENU, 1, 9)

    while input_menu < 9:
        updating_races_file(races_location)
        if input_menu == 1:
            id, time_taken, venue = race_results(races_location)
            fastest_runner = winner_of_race(id, time_taken)
            display_races(id, time_taken, venue, fastest_runner)
        elif input_menu == 2:
            users_venue(races_location, runners_id)
        elif input_menu == 3:
            competitors_by_county(runners_name, runners_id)
        elif input_menu == 4:
            displaying_winners_of_each_race(races_location)
        elif input_menu == 5:
            runner, id = relevant_runner_info(runners_name, runners_id)
            displaying_race_times_one_competitor(races_location, runner, id)
        elif input_menu == 6:
            displaying_runners_who_have_won_at_least_one_race(races_location, runners_name, runners_id)
        elif input_menu == 7:
            read_podium_of_race(races_location)
        elif input_menu ==8:
            read_no_podium(races_location, runners_name, runners_id)
            
        print()
        input_menu = read_integer_between_numbers(MENU, 1, 9)
    updating_races_file(races_location)



def test_rn():
    assert 1 == 1 


main()
