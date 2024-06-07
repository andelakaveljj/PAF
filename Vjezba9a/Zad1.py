import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from planeti import run_simulation

# Konstante
AU = 1.496e11  # Astronomska jedinica (m)
seconds_in_year = 365.242 * 24 * 3600  # Broj sekundi u jednoj godini

# Početni uvjeti za Sunce i Zemlju
bodies = {
    'Sun': {
        'mass': 1.989e30,  # Masa Sunca u kilogramima
        'position': np.array([0.0, 0.0]),  # Početna pozicija Sunca (x, y)
        'velocity': np.array([0.0, 0.0])  # Početna brzina Sunca (vx, vy)
    },
    'Earth': {
        'mass': 5.9742e24,  # Masa Zemlje u kilogramima
        'position': np.array([AU, 0.0]),  # Početna pozicija Zemlje (x, y)
        'velocity': np.array([0.0, 29783.0])  # Početna brzina Zemlje (vx, vy)
    }
}

# Vremenski parametri
time_step = 60 * 60  # Vremenski korak simulacije (jedan sat)
simulation_duration = seconds_in_year / 2  # Trajanje simulacije (pola godine)
num_steps = int(simulation_duration / time_step)  # Ukupan broj koraka simulacije

# Pokretanje simulacije
positions = run_simulation(bodies, time_step, num_steps)  # Poziv funkcije za simulaciju kretanja tijela

# Priprema za animaciju
fig, ax = plt.subplots()  # Inicijalizacija figure i osi za crtanje
ax.set_xlim(-2 * AU, 2 * AU)  # Postavljanje granica osi x
ax.set_ylim(-2 * AU, 2 * AU)  # Postavljanje granica osi y

# Postavljanje linija za Sunce i Zemlju
sun_line, = ax.plot([], [], color='#FFDB58', marker='o', markersize=10, label='Sun')  # Crtanje Sunca
earth_line, = ax.plot([], [], 'bo', markersize=5, label='Earth')  # Crtanje Zemlje
earth_orbit_line, = ax.plot([], [], 'b:', label='Earth Path')  # Putanja Zemlje isprekidana točkama
sun_orbit_line, = ax.plot([], [], color='#FFDB58', linestyle='--', label='Sun Path')  # Putanja Sunca

# Inicijalizacija podataka za putanje
earth_path = np.zeros((num_steps, 2))  # Putanja Zemlje
sun_path = np.zeros((num_steps, 2))  # Putanja Sunca

def init():
    sun_line.set_data([], [])  # Početni podaci za Sunce
    earth_line.set_data([], [])  # Početni podaci za Zemlju
    earth_orbit_line.set_data([], [])  # Početni podaci za putanju Zemlje
    sun_orbit_line.set_data([], [])  # Početni podaci za putanju Sunca
    return sun_line, earth_line, earth_orbit_line, sun_orbit_line  # Vraćanje linija

def update(frame):
    sun_line.set_data(positions['Sun'][frame, 0], positions['Sun'][frame, 1])  # Ažuriranje pozicije Sunca
    earth_line.set_data(positions['Earth'][frame, 0], positions['Earth'][frame, 1])  # Ažuriranje pozicije Zemlje
    
    # Ažuriranje putanja
    earth_path[frame] = positions['Earth'][frame]  # Pohrana trenutne pozicije Zemlje
    sun_path[frame] = positions['Sun'][frame]  # Pohrana trenutne pozicije Sunca
    earth_orbit_line.set_data(earth_path[:frame+1, 0], earth_path[:frame+1, 1])  # Ažuriranje putanje Zemlje
    sun_orbit_line.set_data(sun_path[:frame+1, 0], sun_path[:frame+1, 1])  # Ažuriranje putanje Sunca
    
    return sun_line, earth_line, earth_orbit_line, sun_orbit_line  # Vraćanje linija

animation_func = animation.FuncAnimation(
    fig, update, frames=num_steps, init_func=init, blit=True, interval=0.5
)  # Kreiranje animacije

plt.legend()  # Dodavanje legende
plt.title('Putanja Sunca i Zemlje')  # Postavljanje naslova grafikona
plt.xlabel('X [m]')  # Oznaka x osi
plt.ylabel('Y [m]')  # Oznaka y osi
plt.grid(True)  # Uključivanje mreže
plt.show()  # Prikaz grafikona i animacije
