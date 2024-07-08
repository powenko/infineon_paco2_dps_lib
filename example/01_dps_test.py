from infineon_paco2_dps_lib import dps
 
def main():
    # Create an instance of the dps class
    sensor = dps()
    
    # Read and print the temperature and pressure
    temperature = sensor.read_temperature()
    pressure = sensor.read_pressure()
    
    print(f"Temperature: {temperature:.2f} °C")
    print(f"Pressure: {pressure:.2f} Pa")



if __name__ == "__main__":
    main()
