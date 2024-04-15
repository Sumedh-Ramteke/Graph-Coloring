class CSP:
    def __init__(self, vars, doms, cons):
        self.variables = vars
        self.domains = doms
        self.constraints = cons

    def is_consistent(self, var, val, assignment):
        for neighbor in self.constraints[var]:
            if neighbor in assignment and assignment[neighbor] == val:
                return False
        return True

    def forward_checking(self, var, val, assignment):
        pruned_domains = self.domains.copy()
        for neighbor in self.constraints[var]:
            if neighbor not in assignment:
                pruned_domains[neighbor] = [v for v in pruned_domains[neighbor] if v != val]
                if not pruned_domains[neighbor]:
                    return {}
        return pruned_domains

    def select_unassigned_var(self, assignment):
        unassigned = [v for v in self.variables if v not in assignment]
        return min(unassigned, key=lambda v: len(self.domains[v]))

    def order_domain_values(self, var, assignment):
        values = self.domains[var][:]
        values.sort(key=lambda val: self.num_conflicts(var, val, assignment))
        return values

    def num_conflicts(self, var, val, assignment):
        count = 0
        for neighbor in self.constraints[var]:
            if neighbor in assignment and assignment[neighbor] == val:
                count += 1
        return count

    def backtrack_search(self):
        return self.backtrack({})

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        var = self.select_unassigned_var(assignment)
        for val in self.order_domain_values(var, assignment):
            if self.is_consistent(var, val, assignment):
                new_assignment = assignment.copy()
                new_assignment[var] = val
                pruned_domains = self.forward_checking(var, val, assignment)
                if pruned_domains:
                    self.domains = pruned_domains
                    result = self.backtrack(new_assignment)
                    if result:
                        return result
                    self.domains = self.domains.copy()
        return {}

def australia_map_coloring():
    vars = ["Western Australia", "Northern Territory", "South Australia", "Queensland", "New South Wales", "Victoria", "Tasmania"]
    doms = {v: ["Red", "Green", "Blue", "Yellow"] for v in vars}
    cons = {
        "Western Australia": ["Northern Territory", "South Australia"],
        "Northern Territory": ["Western Australia", "South Australia", "Queensland"],
        "South Australia": ["Western Australia", "Northern Territory", "Queensland", "New South Wales", "Victoria"],
        "Queensland": ["Northern Territory", "South Australia", "New South Wales"],
        "New South Wales": ["South Australia", "Queensland", "Victoria"],
        "Victoria": ["South Australia", "New South Wales", "Tasmania"],
        "Tasmania": ["Victoria"]
    }
    csp = CSP(vars, doms, cons)
    return csp.backtrack_search()

def india_map_coloring():
    vars = ["Andaman and Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chandigarh", "Chhattisgarh", "Dadra and Nagar Haveli and Daman & Diu", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Delhi", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
    doms = {v: ["Red", "Green", "Blue", "Yellow"] for v in vars}
    cons = {
        "Andaman and Nicobar Islands": ["Tamil Nadu"],
        "Andhra Pradesh": ["Karnataka", "Tamil Nadu", "Telangana", "Odisha"],
        "Arunachal Pradesh": ["Assam", "Manipur"],
        "Assam": ["Arunachal Pradesh", "Manipur", "Nagaland", "Meghalaya", "West Bengal"],
        "Bihar": ["Jharkhand", "Uttar Pradesh", "Odisha"],
        "Chandigarh": ["Haryana", "Punjab"],
        "Chhattisgarh": ["Madhya Pradesh", "Odisha", "Jharkhand"],
        "Dadra and Nagar Haveli and Daman & Diu": [],
        "Goa": ["Maharashtra", "Karnataka"],
        "Gujarat": ["Maharashtra", "Madhya Pradesh", "Rajasthan"],
        "Haryana": ["Rajasthan", "Uttar Pradesh", "Punjab", "Chandigarh"],
        "Himachal Pradesh": ["Jammu & Kashmir", "Punjab", "Uttarakhand"],
        "Jammu & Kashmir": ["Himachal Pradesh"],
        "Jharkhand": ["Bihar", "Chhattisgarh", "Odisha", "West Bengal"],
        "Karnataka": ["Andhra Pradesh", "Maharashtra", "Tamil Nadu", "Telangana", "Goa"],
        "Kerala": ["Tamil Nadu"],
        "Ladakh": [],
        "Lakshadweep": [],
        "Madhya Pradesh": ["Chhattisgarh", "Gujarat", "Maharashtra", "Odisha", "Rajasthan", "Uttar Pradesh", "Chandigarh"],
        "Maharashtra": ["Goa", "Gujarat", "Madhya Pradesh", "Karnataka", "Telangana", "Chhattisgarh"],
        "Manipur": ["Assam", "Arunachal Pradesh"],
        "Meghalaya": ["Assam"],
        "Mizoram": ["Odisha", "Tripura"],
        "Nagaland": ["Odisha"],
        "Odisha": ["Andhra Pradesh", "Bihar", "Chhattisgarh", "Jharkhand", "Madhya Pradesh", "Telangana"],
        "Puducherry": [],
        "Punjab": ["Haryana", "Himachal Pradesh", "Rajasthan", "Chandigarh"],
        "Rajasthan": ["Gujarat", "Haryana", "Madhya Pradesh", "Uttar Pradesh", "Punjab"],
        "Sikkim": ["West Bengal"],
        "Tamil Nadu": ["Andhra Pradesh", "Karnataka", "Kerala"],
        "Telangana": ["Andhra Pradesh", "Karnataka", "Maharashtra", "Odisha"],
        "Delhi": [],
        "Tripura": ["Mizoram"],
        "Uttar Pradesh": ["Bihar", "Haryana", "Madhya Pradesh", "Rajasthan", "Uttarakhand", "Chandigarh"],
        "Uttarakhand": ["Himachal Pradesh", "Uttar Pradesh"],
        "West Bengal": ["Assam", "Jharkhand", "Sikkim"]
    }
    csp = CSP(vars, doms, cons)
    return csp.backtrack_search()


def map_coloring_solver(map_choice):
    if map_choice == 1:
        return australia_map_coloring()
    elif map_choice == 2:
        return india_map_coloring()
    else:
        return None

if __name__ == "__main__":
    print("Graph Coloring Map choice:")
    print("\t1. Australia Map")
    print("\t2. India Map")
    choice = int(input("\nEnter your choice..."))
    
    if choice == 1:
        solution = australia_map_coloring()
        print("Solution:")
        for state, color in solution.items():
            print(state, "-->", color)
            
    elif choice == 2:
        solution = india_map_coloring()
        print("Solution:")
        for state, color in solution.items():
            print(state, "-->", color)
    
    else:
        print("Invalid Choice!")
