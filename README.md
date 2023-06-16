# network-analysis
This Python script provides a comprehensive network traffic analysis solution by leveraging the power of Python libraries such as Pandas, Matplotlib, and Networkx. With this script, you can gain insights into network communication patterns, identify potential security threats, and visualize the network topology.

The script takes a CSV file containing network traffic data as input. You can obtain this data from sources like Wireshark (as I did), which captures and analyzes network packets. Once the data is loaded, the script performs various analysis tasks to help you understand the network activity.

Key features:
- Grouping and counting devices based on communication frequency: The script identifies devices that initiate and accept the most communications, giving you    
  insights into the network's key players.
- Analyzing communication protocols: It identifies the types of protocols used in the network, such as HTTP or HTTPS, to determine if any sensitive information is 
  being transmitted unencrypted.
- Creating network graphs: By utilizing the Networkx library, the script visualizes the network topology as a graph, showcasing how devices communicate with each 
  other.
- Suspect device identification: You can flag a suspicious device by providing its IP address. The script highlights the suspect in the network graph and provides 
  a new dataframe with information about the suspect's communication activities.
- By using this script, network administrators, cybersecurity professionals, and anyone interested in network analysis can gain valuable insights into network 
  traffic, identify potential security risks, and optimize network performance.
