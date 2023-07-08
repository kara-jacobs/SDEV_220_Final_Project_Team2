##### describes anyone who uses the app.
class User():
    def __init__(self, name, age):
        self.name = name # first, middle, and last name
        self.age = age

    # a function that adds the user to RSVP list of an event. 
    def RSVP():
        pass 
    
    # a function that removes the user from an events RSVP list. 
    def un_RSVP():
        pass


##### a subclass of user that can add events.
class Host(User):
    def __init__(self, name, age, contact_info):
        super().__init__(name, age)
        self.contact_info = contact_info # must have listed contact info.

    # add an event to the calendar (This is the big one) 
    def add_event():
        pass 
    
    # cancels an event that the host had previously scheduled. 
    def remove_event():
        pass

    # edits an event that the host had previously scheduled. 
    def edit_event():
        pass


##### a collection of users? Honestly I'm still workshopping this.
class Group():
    def __init__(self, name, contact_info, members_list, authority):
        self.name = name
        self.contact_info = contact_info
        self.members_list = members_list
        self.authority = authority

    def approve_event():
        pass

    def add_member():
        pass

    def remove_member():
        pass


##### All the information for an event. The main meat of the program and the reason we are here.
class Event():
    def __init__(self, name, description, timeslot, host, fee, 
                capacity, RSVP_list, sanction_status):
        self.name = name # name of the event
        self.age = description # doc string that talks about the event
        self.timeslot = timeslot # when the event is happening
        self.host = host # who is responsible for the event
        self.fee = fee # says if there is an entry fee for attending the event.   
        self.capacity = capacity # how many people can attend the event
        self.RSVP_list = RSVP_list # a list of people who have RSVPed to the event.
        # when displayed show as the length of the list rather than the list itself
        self.sanction_status = sanction_status # says if the event is approved by the city. 
        # (needed if the even has an entry fee?) I'll be honest 
        # am hurting to pad out our number of classes because I am unsure if subclasses count. 