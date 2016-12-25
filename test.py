import neurio
import neurio_keys

# Setup authentication:
tp = neurio.TokenProvider(key=neurio_keys.key, secret=neurio_keys.secret)
# Create client that can authenticate itself:
nc = neurio.Client(token_provider=tp)
# Get user information (including sensor ID and location ID)
user_info = nc.get_user_information()

print("Sensor ID {}, location ID {}".format(user_info["locations"][0]["sensors"][0]["sensorId"],
  user_info["locations"][0]["id"]))

# Fetch sample:
sample = nc.get_samples_live_last(sensor_id=neurio_keys.sensor_id)

print(sample)

print("Current power consumption: {} W".format(sample['consumptionPower']))

sample = nc.get_local_current_sample("192.168.1.7")

print(sample)
