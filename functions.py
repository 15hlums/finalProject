# changes the arrival time with respect to the delay
def delay_changetime(delay, arrival_time):
    t = delay
    (m, s) = t.split(':')
    num = int(m) * 60 + int(s)
    current_time = arrival_time
    current_min = (current_time[3] + current_time[4])
    current_hour = (current_time[0] + current_time[1])
    added_hour = 0

    # if the minutes plus the delay time is less than an hour
    if (int(current_min) + int(num)) < 60:
        final_min = str(int(current_min) + int(num))
        if len(final_min) == 1:
            final_time = (current_time[0] + current_time[1] + current_time[2] + '0' + final_min[0])
            return final_time
        else:
            final_time = (current_time[0] + current_time[1] + current_time[2] + final_min[0] + final_min[1])
            return final_time

    # if the minutes plus the delay time is larger than an hour (carries over to next hour)
    elif (int(current_min) + int(num)) > 60:
        # if the hour is 23:00
        if int(current_hour) == 23:
            final_min = str((int(current_min) + int(num)) - 60)
            final_hour = '0'
            if len(final_min) == 1:
                final_time = (final_hour[0] + final_hour[0] + current_time[2] + '0' + final_min[0])
                return final_time
            else:
                final_time = (final_hour[0] + final_hour[0] + current_time[2] + final_min[0] + final_min[1])
                return final_time

        # if the hour is not 23:00
        else:
            # if the hour is less than 09:00
            if int(current_hour) < 9:
                final_min = str(int(current_min) + int(num))
                while int(final_min) >= 60:
                    final_min = str(int(final_min) - 60)
                    added_hour += 1
                final_hour = str(int(current_hour[0] + current_hour[1]) + added_hour)
                if len(final_min) == 1:
                    final_time = ('0' + str(final_hour[0] + current_time[2] + '0' + final_min[0]))
                    return final_time
                else:
                    final_time = ('0' + str(final_hour[0] + current_time[2] + final_min[0] + final_min[1]))
                    return final_time

            # if the hour is or greater than 09:00
            else:
                final_min = str(int(current_min) + int(num))
                while int(final_min) >= 60:
                    final_min = str(int(final_min) - 60)
                    added_hour += 1
                final_hour = str(int(current_hour[0] + current_hour[1]) + added_hour)
                if len(final_min) == 1:
                    if len(final_hour) == 1:
                        final_time = (str(final_hour[0] + '0' + current_time[2] + '0' + final_min[0]))
                        return final_time
                    else:
                        final_time = (str(final_hour[0] + final_hour[1] + current_time[2] + '0' + final_min[0]))
                        return final_time
                else:
                    if len(final_hour) == 1:
                        final_time = (str(final_hour[0] + '0' + current_time[2] + final_min[0] + final_min[1]))
                        return final_time
                    else:
                        final_time = (
                            str(final_hour[0] + final_hour[1] + current_time[2] + final_min[0] + final_min[1]))
                        return final_time


    # if the minutes plus the delay time is exactly an hour
    elif (int(current_min) + int(num)) == 60:
        # if the hour is 23:00
        if int(current_hour) == 23:
            final_hour = '0'
            final_time = (final_hour[0] + final_hour[0] + current_time[2] + final_hour[0] + final_hour[0])
            return final_time

        # if the hour is not 23:00
        else:
            # the hour is less than 09:00
            if int(current_hour) < 9:
                final_min = str((int(current_min) + int(num)) - 60)
                final_hour = str(int(current_hour) + 1)
                final_time = ('0' + str(final_hour[0] + current_time[2] + final_min[0] + final_min[0]))
                return final_time

            # if the hour is or greater than 09:00
            else:
                final_min = str((int(current_min) + int(num)) - 60)
                final_hour = str(int(current_hour) + 1)
                final_time = (str(final_hour[0] + final_hour[1] + current_time[2] + final_min[0] + final_min[0]))
                return final_time

# converts time (string) to minutes (integer)
def time_convertmin(time):
    hour_initial = int(time[0] + '0') + int(time[1])
    min_initial = int((time[3]) + (time[4]))
    hour_final = hour_initial * 60
    time_final = hour_final + min_initial
    return time_final

def get_gatenum(gates, row):
    possible_gates = []
    clash_gates = []
    for i in range(0, len(gates)):
        if gates[i] != row[0]:
            # updates database with new gate number
            print()
            print(gates[i])
            print(row)
            possible_gates.append(gates[i])
            print(possible_gates)
            print(clash_gates)

        else:
            print()
            clash_gates.append(gates[i])
            print(clash_gates)

