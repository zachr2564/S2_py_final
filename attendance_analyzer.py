###########################
### Attendance Analyzer ###
###########################


#### Need to take date time, convert to second count, 

#Network x, math plot lib

#get data from sheets, pick target id, 

import networkx as nx
import matplotlib.pyplot as plt
import math



def file_data_extractor_singular(file_path = r'E:\Schoolwork\CS\S2 (Python)\Attendance Analyzer\attendance_sheets\06.01.2024.csv'):         #reads and extracts data from frequency sheet
    with open(file_path, 'r') as data:
        lines = data.readlines()
        attendee_dict_day_n = {}
        for line in lines[1:]:
            line = line.strip()
            line = line.split(',')
            line[0], line[1] = int(line[1]), line[0]                                            #swaps date and id number, converts id to int
            substitutionary_time = line[1].split(':')                                           #splits time HH:MM by :
            time = int(substitutionary_time[0])*3600 + int(substitutionary_time[1])*60          #converts time to seconds
            line[1] = time     
            
            attendee_dict_day_n[line[0]] = line[1:]

        #print(attendee_dict_day_n[101][0])
            
        #print(attendee_dict_day_n)
        return attendee_dict_day_n

#print(file_data_extractor_singular(r'E:\Schoolwork\CS\S2 (Python)\Attendance Analyzer\attendance_sheets\06.05.2024.csv'))



#file paths stored in file, will add to list so that file_data_extractor_singular() can work for each.
def file_path_grabber(file_path_txt_file = r'E:\Schoolwork\CS\S2 (Python)\Attendance Analyzer\attendance_sheets\attendance_sheets_list.csv'):
    file_path_list = []
    with open(file_path_txt_file) as data:
        lines = data.readlines()
        for line in lines[1:]:
            line = line.strip()
            file_path_list.append(line)
    return file_path_list


#extract from each list time of arrival using


def name_getter():                      #go through each file and map a name to an id
    id_name_dict = {}
    file_path_list = file_path_grabber()
    for file in file_path_list:
        with open(file, 'r') as data:
            lines = data.readlines()
            for line in lines[1:]:
                line = line.strip()
                line = line.split(',')
                if int(line[1]) not in id_name_dict:
                    id_name_dict[int(line[1])] = line[2]
    #print(id_name_dict)
    return id_name_dict

#name_getter()



'''

def file_reader_big():
    file_paths = file_path_grabber()
    for i in range(len(file_paths)):
        file_path = file_paths[i]
        print(file_data_extractor_singular(file_path))
'''


def single_sheet_magnitude_measurerer(target_id, file_path = r'E:\Schoolwork\CS\S2 (Python)\Attendance Analyzer\attendance_sheets\attendance_sheets_list.csv'):     #gets member id and toa for a given file
    data = file_data_extractor_singular(file_path)
    member_full_info_dict = data                            #holds onto member data full
    member_id_and_time_dict = {}
    for member in data:                                     #for member id, get corresponding data
        full_data = data[member]                            #does the above
        time = full_data[0]                                 #trims to be just toa
        
        member_id_and_time_dict[member] = time

    
    
    if target_id in member_full_info_dict:
        target_member_toa = member_id_and_time_dict[target_id]  #gets target member toa

        for member_id in member_id_and_time_dict:                                                   #iterates through members
            if member_id != target_id:                                                              #if not the target member
                member_id_and_time_dict[member_id] -= target_member_toa                             #get magnitude of difference between target member and all other toa's
                member_id_and_time_dict[member_id] = abs(member_id_and_time_dict[member_id])        #take abs value of this difference

    else:
        for id in member_full_info_dict:
            member_full_info_dict[id] = 0

    #print(member_id_and_time_dict)
    
    return member_id_and_time_dict

#single_sheet_magnitude_measurerer()




def times_together_getter(target_id):         # finds out how many seperate days the target visited with others
    freq_master_dict = {}                   # our dict listing how many times each visited
    file_path_list = file_path_grabber()    # all data sheets
    all_ids_dict = name_getter()            # all ids
    for id in all_ids_dict:                 # sets times visited for each id to 0
        freq_master_dict[id] = 0

    for file in file_path_list:             # if target visited that day, all else who visited + 1
        todays_attendees = single_sheet_magnitude_measurerer(target_id, file)
        if target_id in todays_attendees:
            for id in todays_attendees:
                freq_master_dict[id] += 1
    
    return freq_master_dict

#times_together_getter()



def times_present_at_all():
    times_present_master_dict = {}                   # our dict listing how many times each visited
    file_path_list = file_path_grabber()    # all data sheets
    all_ids_dict = name_getter()            # all ids
    for id in all_ids_dict:                 # sets times visited for each id to 0
        times_present_master_dict[id] = 0

    for file in file_path_list:             # if target visited that day, all else who visited + 1
        with open(file, 'r') as data:
            lines = data.readlines()
            for line in lines[1:]:
                line = line.split(',')
                times_present_master_dict[int(line[1])] += 1
    
    return times_present_master_dict

#times_present_at_all()





def magnitude_measurer_cumulative(target_id):                             #iterates through all files
    file_paths_list = file_path_grabber()                                       #establishes a list of file paths
    #print(file_paths_list)                                                      #prints this list
    num_file_paths = len(file_paths_list)                                       #gets number of file paths
    times_id_appeared_dict = {}                                                 #how many times did person appear
    master_distance_dict = {}                                                   #aggregates distance from target
    
    for file in file_paths_list:                                                #picks a file path from the list, then proceeds to extract info from it 
        temp_id_and_time_dict = single_sheet_magnitude_measurerer(target_id, file)    #returns dict of id and time for each file
        
        #IMPORTANT      |||     since measuring avg distance when present, only includes times target was present to keep even count
        if target_id in temp_id_and_time_dict:


            for id in temp_id_and_time_dict:                                        #for each id in a given file, check if a log exists
                if id not in master_distance_dict:                                  #if has not been logged yet
                    master_distance_dict[id] = temp_id_and_time_dict[id]            #logged, distance from target = this instance only
                    times_id_appeared_dict[id] = 1                                  #first time this id appeared, so times appeared = 1
                
                    
                elif id in master_distance_dict:                                    #if id has been logged
                    master_distance_dict[id] += temp_id_and_time_dict[id]           #master distance sum increased (will be averaged later)
                    times_id_appeared_dict[id] += 1                                 #time appeared +1
                    
                
    for id in master_distance_dict:
        master_distance_dict[id] = master_distance_dict[id] // times_id_appeared_dict[id]   #gets average distance of time
    
    return master_distance_dict

#print(magnitude_measurer_cumulative())









#could rotate each node around core, lets say take 18 different i+j combos around the circle, multiply by SM for times together, with closest being max

def proximity_visualizer(target_id):                              #proximity dictated by number of days together, edge thickness dictated by avg proximity (seconds)
    master_distance_dict = magnitude_measurer_cumulative(target_id)     #use for thickness
    master_id_name_dict = name_getter()                                 
    master_times_together_dict = times_together_getter(target_id)                #use for distance
    master_times_present_at_all_dict = times_present_at_all()           #how many times showed up at all
    id_list_for_nodes = []
    freq_colors = []
    node_size_list = []   
    text_color_list = []
    
    
    G = nx.Graph()                                                      #consider re-evaluating graph type to enable algorithmic placement of nodes


    id_grand_master_info_dict = {}

    for id in master_id_name_dict:                                      #defines grand compilation of datapoints
        times_together_ratio = master_times_together_dict[id]/master_times_present_at_all_dict[id]
        id_grand_master_info_dict[id] = [master_id_name_dict[id], master_distance_dict[id], master_times_together_dict[id] , master_times_present_at_all_dict[id], times_together_ratio]
        #           id                            name                     distance                    times together                  times present                 together/present
        id_list_for_nodes.append(id)
        


    G.add_node(target_id)
    node_size_list.append(2400)
    freq_colors.append('cyan')
    #text_color_list.append('#ffff00')

    for id in id_list_for_nodes:
        if id not in G:#id != target_id:
            G.add_edge(id, target_id, weight = (id_grand_master_info_dict[id][2])*10)          #closer if together together more

        if id != target_id:
            


            if id_grand_master_info_dict[id][4] <0.25:
                freq_colors.append('red')
                #text_color_list.append('#000000')
            
            elif id_grand_master_info_dict[id][4] <0.5:
                freq_colors.append('yellow')
                #text_color_list.append('#000000')
            
            elif id_grand_master_info_dict[id][4] <0.75:
                freq_colors.append('green')
                #text_color_list.append('#000000')
            
            else:
                freq_colors.append('blue')
                #text_color_list.append('#000000')



    for id in id_grand_master_info_dict:
        if id != target_id:
            temp_size = (((id_grand_master_info_dict[id][1])**-1)*5000000)
            node_size_list.append(int(temp_size))
    
    nx.draw_spring(G, node_size = node_size_list, node_color = freq_colors, edge_color = 'white', edgecolors = 'black', node_shape = 'o', labels = master_id_name_dict, with_labels = True)       #default form, change spring
    plt.show()
    #print(id_grand_master_info_dict)

proximity_visualizer(101)


#https://networkx.org/documentation/stable/auto_examples/drawing/plot_custom_node_icons.html
#https://networkx.org/documentation/stable/auto_examples/drawing/plot_labels_and_colors.html
#https://stackoverflow.com/questions/24636015/networkx-change-node-size-based-on-list-or-dictionary-value

