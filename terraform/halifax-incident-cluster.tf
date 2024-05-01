provider "google" {
    project = "halifaxincident"
    region = "us-east1-b"
}

resource "google_container_cluster" "halifaxincident" {
    name                = "halifax-incident-cluster"
    location            = "us-east1-b"
    initial_node_count  = 1

    node_config {
        machine_type = "e2-medium"
        disk_size_gb = 10
        dist_type = "pd-standard"
        image_type = "COS_CONTAINERD"
    }

    network = "default"
    subnetwork = "default"

}

