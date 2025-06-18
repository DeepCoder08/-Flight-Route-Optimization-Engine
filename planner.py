from flight import Flight

def comp_1(tup1, tup2):

    if tup1[0] < tup2[0]:
        return True
    
    elif tup2[0] < tup1[0]:
        return False
    
    elif tup1[0] == tup2[0]:
        if tup1[1]<tup2[1]:
            return True
        else:
            return False


class Heap: #min heap taken from assignment 3 to implement priority queue for BFS
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        
        
        # Write your code here

        self.comparator= comparison_function
        self.heap= init_array
        self.build_min_heap()
        
    def parent(self, i):
        # Return the parent index of the node at index i
        return (i - 1)//2
    

    def left_child(self, i):
        # Return the left child index of the node at index i
        return 2 * i + 1

    def right_child(self, i):
        # Return the right child index of the node at index i
        return 2 * i + 2
    
    def _heapify_up(self, i):
        # Heapify upwards (restore heap property going upwards from node i)
        compare= self.comparator(self.heap[self.parent(i)], self.heap[i])
        while i != 0 and not compare:
            # Swap the current node with its parent
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
 
    def _heapify_down(self, i):
        # Heapify downwards (restore heap property going downwards from node i)
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        # Find the smallest among root, left child, and right child
        
        if left < len(self.heap) and self.comparator(self.heap[left], self.heap[smallest]):
            smallest = left
        if right < len(self.heap) and self.comparator(self.heap[right], self.heap[smallest]):
            smallest = right
        
        # If the smallest is not the root, swap and continue heapifying
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

    def build_min_heap(self):
        # Convert the array into a min-heap in O(n) time
        n = len(self.heap)
        # Start heapifying from the last non-leaf node and go upwards
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)

    def size(self):
        # Return the size of the heap
        return len(self.heap)
        
    def insert(self, value):

        # Insert a new key into the heap
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
        
        # Write your code here
        pass

    def print_heap(self):
        print(self.heap)
   
    def extract(self):

        # Remove and return the minimum element (root) from the heap
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Replace the root with the last element, and remove the last element
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        # Restore the heap property
        self._heapify_down(0)
        return root

        
        # Write your code here
        
    
    def top(self):   
        # Write your code here
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def is_empty(self):
        if len(self.heap)==0:
            return True
        else:
            return False

class Planner:
    def __init__(self, flights):
        """The Planner

        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        self.m= len(flights) #no of flights
        self.flight_adj_list= [None]*(len(flights)) #as no of cities is O(m)
        for i in range(len(flights)):
            x= flights[i].start_city
            if self.flight_adj_list[x]==None:
                self.flight_adj_list[x]= [flights[i]]
                

            else:
                (self.flight_adj_list[x]).append(flights[i])

        #each city stores a list of outgoing/departing flights
        #we implemented the graph data structure using adjacency list in O(m)




        pass
    
    def least_flights_ealiest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        # Priority queue to store tuples of (number_of_flights, arrival_time, current_city, route_taken)
        #rout_taken is a list of the cities visited

        queue = Heap(comp_1,[])
        queue.insert((0, t1, start_city, []))

        visited= [0]*(self.m) #to keep a track of cities visited

        

        while not queue.is_empty():

            num_flights, arrival_time, current_city, route_taken = queue.extract()

            if current_city== end_city:
                return route_taken 
            
            if visited[current_city] !=0 and visited[current_city]< num_flights:
                continue
            visited[current_city]= num_flights

            # Explore all flights departing from the current city
            count=0
            if self.flight_adj_list[current_city]:
                for fly in self.flight_adj_list[current_city]:
                    # Check connection conditions
                    if current_city== start_city:
                        count=1
                        if (fly.departure_time >= t1 and fly.arrival_time <= t2):  # Sufficient layover of more than 20 minutes or so
                        # and Within time limits
                    
                        # Enqueue with updated parameters
                            new_route = route_taken + [fly]
                            queue.insert((num_flights + 1, fly.arrival_time, fly.end_city, new_route))

                    else:
                        if (fly.departure_time >= arrival_time + 20 and fly.departure_time >= t1 and fly.arrival_time <= t2):  # Sufficient layover of more than 20 minutes or so
                        # and Within time limits
                    
                        # Enqueue with updated parameters
                            new_route = route_taken + [fly]
                            queue.insert((num_flights + 1, fly.arrival_time, fly.end_city, new_route))                   

        




        pass
    
    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        queue = Heap(comp_1,[])
        #we insert tuples of the form (fare_spent, arrival time, current city, route taken into this minheap)
        queue.insert((0, t1, start_city,[] ))

        visited= [0]*(self.m) #to keep a track of cities visited

        

        while not queue.is_empty():

            fare, arrival_time, current_city, route_taken = queue.extract()

            if current_city== end_city:
                return route_taken 
            
            if visited[current_city] !=0 and visited[current_city]< fare:
                continue
            visited[current_city]= fare

            # Explore all flights departing from the current city
            if self.flight_adj_list[current_city]:
                for flight in self.flight_adj_list[current_city]:
                    # Check connection conditions

                    if current_city== start_city:
                        if (flight.departure_time >= t1 and flight.arrival_time <= t2):  # Sufficient layover of more than 20 minutes or so
                        # and Within time limits
                    
                        # Enqueue with updated parameters
                            new_route = route_taken + [flight]
                            queue.insert((fare + flight.fare, flight.arrival_time, flight.end_city, new_route))

                    else:
                        if (flight.departure_time >= arrival_time + 20 and flight.departure_time >= t1 and flight.arrival_time <= t2):  # Sufficient layover of more than 20 minutes or so
                        # and Within time limits
                    
                        # Enqueue with updated parameters
                            new_route = route_taken + [flight]
                            queue.insert((fare + flight.fare, flight.arrival_time, flight.end_city, new_route))                   

        # If we exhaust the queue without finding a route, that is no route exists between two cities
        return None



        pass
    
    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """

        queue = Heap(comp_1,[])
        queue.insert((0, 0,t1, start_city, []))

        visited= [0]*(self.m) #to keep a track of cities visited

        

        while not queue.is_empty():

            num_flights,tot_fare, arrival_time, current_city, route_taken = queue.extract()

            if current_city== end_city:
                return route_taken 
            
            if visited[current_city] !=0 and visited[current_city]< num_flights:
                continue
            visited[current_city]= num_flights

            # Explore all flights departing from the current city

            if self.flight_adj_list[current_city]:
                for fly in self.flight_adj_list[current_city]:
                    # Check connection conditions

                    if current_city== start_city:

                        if ( fly.departure_time >= t1 and fly.arrival_time <= t2):  # Sufficient layover of more than 20 minutes or so
                            # and Within time limits
                    
                            # Enqueue with updated parameters
                            new_tot_fare= tot_fare+ fly.fare
                            new_route = route_taken + [fly]
                            queue.insert((num_flights + 1,new_tot_fare, fly.arrival_time, fly.end_city, new_route))
                
                    else:
                        if (fly.departure_time >= arrival_time + 20 and fly.departure_time >= t1 and fly.arrival_time <= t2):  # Sufficient layover of more than 20 minutes or so
                        # and Within time limits
                    
                        # Enqueue with updated parameters
                            new_tot_fare= tot_fare+ fly.fare
                            new_route = route_taken + [fly]
                            queue.insert((num_flights + 1,new_tot_fare, fly.arrival_time, fly.end_city, new_route))
                

        # If we exhaust the queue without finding a route, that is no route exists between two cities
        return None

        pass