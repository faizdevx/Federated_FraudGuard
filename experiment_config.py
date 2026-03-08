# experiment_config.py
# Global experiment configuration for Federated Fraud Detection
# Commit to this configuration BEFORE implementing models

EXPERIMENT_CONFIG = {

    # -------------------------------------------------------
    # Reproducibility
    # -------------------------------------------------------
    "seed": 42,
    "seeds": [42, 123, 999],  # multiple runs for statistical stability

    # -------------------------------------------------------
    # Dataset
    # -------------------------------------------------------
    "dataset": "ieee_cis_fraud",
    "train_split": 0.7,
    "val_split": 0.1,
    "test_split": 0.2,

    # Partition strategy
    "partition": {
        "iid_method": "random",
        "noniid_method": "addr1_cluster",   # realistic geographic partition
        "n_clients": 20
    },

    # -------------------------------------------------------
    # Federated Learning Settings
    # -------------------------------------------------------
    "fl": {
        "rounds": 50,
        "local_epochs": 1,
        "batch_size": 256,
        "learning_rate": 0.01
    },

    # -------------------------------------------------------
    # Privacy Configuration (Gap 3)
    # -------------------------------------------------------
    "differential_privacy": {
        "enabled": True,
        "epsilon_grid": [1, 3, 5, 10],
        "delta": 1e-5,
        "clip_norm": 1.0
    },

    # -------------------------------------------------------
    # Byzantine Attack Configuration (Gap 2)
    # -------------------------------------------------------
    "byzantine": {
        "enabled": True,
        "attack_type": "gradient_flip",
        "client_fraction": 0.2   # 20% malicious clients
    },

    # -------------------------------------------------------
    # Aggregation Methods
    # -------------------------------------------------------
    "aggregation": {
        "fedavg": "standard_mean",
        "fedmedian": "coordinate_median"
    },

    # -------------------------------------------------------
    # Experiment Conditions (8-condition matrix)
    # Each condition addresses one research gap
    # -------------------------------------------------------
    "conditions": [

        # Gap 1 — Literature baselines
        {
            "name": "centralized_lr",
            "type": "centralized",
            "model": "logistic_regression"
        },

        {
            "name": "centralized_rf",
            "type": "centralized",
            "model": "random_forest"
        },

        {
            "name": "centralized_lgbm",
            "type": "centralized",
            "model": "lightgbm"
        },

        # Gap 1 — IID control
        {
            "name": "fedavg_iid",
            "type": "federated",
            "partition": "iid",
            "aggregation": "fedavg",
            "dp": False,
            "byzantine": False
        },

        # Gap 1 — realistic non-IID environment
        {
            "name": "fedavg_noniid",
            "type": "federated",
            "partition": "noniid",
            "aggregation": "fedavg",
            "dp": False,
            "byzantine": False
        },

        # Gap 3 — privacy tradeoff
        {
            "name": "fedavg_dp",
            "type": "federated",
            "partition": "noniid",
            "aggregation": "fedavg",
            "dp": True,
            "byzantine": False
        },

        # Gap 2 — robustness test
        {
            "name": "fedmedian_byzantine",
            "type": "federated",
            "partition": "noniid",
            "aggregation": "fedmedian",
            "dp": False,
            "byzantine": True
        },

        # YOUR METHOD — all gaps together
        {
            "name": "fedmedian_dp_byzantine",
            "type": "federated",
            "partition": "noniid",
            "aggregation": "fedmedian",
            "dp": True,
            "byzantine": True
        }
    ],

    # -------------------------------------------------------
    # Evaluation Metrics
    # -------------------------------------------------------
    "metrics": [

        # Fraud detection metrics
        "pr_auc",
        "roc_auc",
        "recall_at_1fpr",
        "f1_score",
        "false_positive_rate",

        # Privacy evaluation
        "mia_auc",          # membership inference attack success

        # System metrics
        "bytes_per_round",  # communication cost
        "training_time",

        # Business metric
        "cost_savings"
    ]
}