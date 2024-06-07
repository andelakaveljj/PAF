import numpy as np

gravitational_constant = 6.67408e-11  # Gravitacijska konstanta u Nm^2/kg^2

def compute_gravitational_force(mass1, mass2, pos1, pos2):
    vector_distance = pos2 - pos1
    dist_magnitude = np.linalg.norm(vector_distance)
    if dist_magnitude == 0:
        return np.array([0.0, 0.0])
    force_strength = gravitational_constant * mass1 * mass2 / dist_magnitude**2
    direction_vector = vector_distance / dist_magnitude
    return force_strength * direction_vector

def run_simulation(bodies, timestep, total_steps):
    trajectories = {body_name: np.zeros((total_steps, 2)) for body_name in bodies}
    
    for step in range(total_steps):
        net_forces = {body_name: np.array([0.0, 0.0]) for body_name in bodies}
        
        for body1_name, body1 in bodies.items():
            for body2_name, body2 in bodies.items():
                if body1_name != body2_name:
                    net_forces[body1_name] += compute_gravitational_force(
                        body1['mass'], body2['mass'], body1['position'], body2['position']
                    )
        
        for body_name, body in bodies.items():
            acceleration = net_forces[body_name] / body['mass']
            body['velocity'] += acceleration * timestep
            body['position'] += body['velocity'] * timestep
            trajectories[body_name][step] = body['position']
    
    return trajectories