import random

class TicketGenerator:
    pastTickets = [
        (14, 15, 16, 39, 42),
        (6, 10, 13, 17, 31),
        (5, 6, 23, 33, 45),
        (11, 15, 37, 40, 46),
        (5, 7, 20, 43, 48),
        (9, 13, 34, 36, 46),
        (19, 24, 28, 33, 39),
        (2, 10, 40, 47, 48),
        (2, 10, 15, 35, 47),
        (6, 12, 16, 19, 22),
        (1, 8, 18, 27, 46),
        (13, 33, 34, 43, 44),
        (1, 6, 16, 27, 34),
        (25, 28, 32, 47, 48),
        (9, 24, 25, 29, 42),
        (26, 29, 31, 34, 40),
        (9, 18, 24, 26, 29),
        (5, 15, 30, 40, 45)]

    max_num = 48
    num_count = 5
    match_threshold = 4

    @classmethod
    def generate(cls):
        newTicket = random.sample(range(TicketGenerator.max_num), TicketGenerator.num_count)
        for oldTicket in TicketGenerator.pastTickets:
            matches = set(oldTicket).intersection(newTicket)
            matchCount = len(matches)
            if matchCount >= TicketGenerator.match_threshold:
                print("%s and %s match on %s" % (newTicket, oldTicket, matches))
                return TicketGenerator.generate()
        return newTicket
