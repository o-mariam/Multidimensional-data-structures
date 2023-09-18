# Multidimensional Data Structures: DHT-based File Sharing System

Welcome to the repository dedicated to the experimental study of a Distributed Hash Table (DHT) based file sharing system using the Chord protocol. This is a part of the multidimensional data structures project focusing on DHTs using the Chord protocol.

---

## Project Description:

The main objective of this project is to conduct an experimental study on the performance of fundamental operations within the context of DHTs (Chord). The dataset used is derived from the [GFZ German Research Centre for Geosciences](http://gmo.gfz-potsdam.de/pub/gshap_data/gshap_data_frame.html), where the "value" corresponds to a set of attributes associated with the key.

---

## Key Operations:

1. **Insert Key**: Insert a new key into the DHT.
  
2. **Delete Key**: Remove a key from the DHT.

3. **Update Record**: Modify the record based on a specific key.

4. **Node Join**: Add a new node to the network.

5. **Node Leave**: Gracefully remove a node from the network.

6. **Massive Node Failure**: Simulate the sudden failure of multiple nodes.

7. **Exact Match**: Search for an exact match based on the key.

8. **Range Queries**: Search for keys within a specified range.

9. **kNN Queries**: Execute k-Nearest Neighbor queries.

---

## Dataset:

The data used for the experiments comes from the GFZ German Research Centre for Geosciences. You can access and review the dataset [here](http://gmo.gfz-potsdam.de/pub/gshap_data/gshap_data_frame.html). In this context, the "value" for each key in the DHT consists of a set of attributes that are related to the key.

---

## Getting Started:

### Prerequisites:

- Ensure you have the necessary libraries and tools installed to run a DHT system.
- A basic understanding of the Chord protocol.

### Running the System:

1. **Clone the Repository**:
   ```
   git clone https://github.com/YOUR-USERNAME/Multidimensional-data-structures.git
   ```

2. **Navigate to the Directory**:
   ```
   cd Multidimensional-data-structures
   ```

3. **Execute the Main Script**:
   ```
   python main_script.py
   ```

---

## Results & Analysis:

Upon executing the different operations, the system will display the performance results, providing insights into the efficiency and effectiveness of the DHT using the Chord protocol on the given dataset.

---
