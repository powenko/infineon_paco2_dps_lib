from infineon_paco2_dps_lib import paco2

def main():
    # Initialize the pa_co2 sensor
    sensor = paco2()

    # Measure CO2 concentration
    co2_concentration = sensor.measure_co2()
    print(f"CO2 Concentration: {co2_concentration:.2f} ppm")

if __name__ == "__main__":
    main()
