import pandas as pd
import numpy as np

from datetime import datetime
from datetime import timedelta

np.random.seed(42)

# ==========================================
# CONFIG
# ==========================================

N_SEARCH_QUERIES = 10000
N_CAMPAIGNS = 5000
N_VISIBILITY = 3000
N_EXPERIMENTS = 1000

# ==========================================
# SEARCH QUERIES
# ==========================================

queries = [

    "best cashback credit card",
    "travel rewards card",
    "business credit card",
    "premium credit card",
    "airport lounge access card",
    "student credit card",
    "best rewards card",
    "credit card for startups",
    "small business credit card",
    "best travel card"

]

start_date = datetime(
    2024,
    1,
    1
)

dates = [

    start_date +
    timedelta(
        days=np.random.randint(
            0,
            730
        )
    )

    for _
    in range(
        N_SEARCH_QUERIES
    )

]

search_df = pd.DataFrame({

    "Date": dates,

    "Query": np.random.choice(
        queries,
        N_SEARCH_QUERIES
    ),

    "Impressions": np.random.randint(
        100,
        10000,
        N_SEARCH_QUERIES
    ),

    "Clicks": np.random.randint(
        10,
        2000,
        N_SEARCH_QUERIES
    ),

    "Conversions": np.random.randint(
        1,
        200,
        N_SEARCH_QUERIES
    ),

    "Spend": np.random.uniform(
        50,
        5000,
        N_SEARCH_QUERIES
    ).round(2),

    "Revenue": np.random.uniform(
        200,
        20000,
        N_SEARCH_QUERIES
    ).round(2)

})

search_df.to_csv(
    "datasets/search_queries.csv",
    index=False
)

# ==========================================
# CAMPAIGNS
# ==========================================

products = [
    "Travel",
    "Cashback",
    "Business",
    "Gold",
    "Platinum"
]

audiences = [
    "Prospecting",
    "Remarketing",
    "High Value",
    "SMB",
    "Students"
]

devices = [
    "Mobile",
    "Desktop"
]

campaign_names = []

for product in products:
    for audience in audiences:
        for device in devices:

            campaign_names.append(
                f"{product}_{audience}_{device}"
            )

campaign_df = pd.DataFrame({

    "Campaign_ID":

        range(
            1,
            N_CAMPAIGNS + 1
        ),

    "Campaign_Name":

        np.random.choice(
            campaign_names,
            N_CAMPAIGNS
        ),

    "Products" : 
        np.random.choice(
            ["Travel",
            "Cashback",
            "Business",
            "Gold",
            "Platinum"],
            N_CAMPAIGNS
        ),

    "Device":

        np.random.choice(
            [
                "Mobile",
                "Desktop",
                "Tablet"
            ],
            N_CAMPAIGNS
        ),

    "Impressions":

        np.random.randint(
            1000,
            100000,
            N_CAMPAIGNS
        ),

    "Clicks":

        np.random.randint(
            100,
            10000,
            N_CAMPAIGNS
        ),

    "Conversions":

        np.random.randint(
            10,
            1000,
            N_CAMPAIGNS
        ),

    "Spend":

        np.random.uniform(
            500,
            25000,
            N_CAMPAIGNS
        ).round(2),

    "Revenue":

        np.random.uniform(
            1000,
            100000,
            N_CAMPAIGNS
        ).round(2)

})

campaign_df.to_csv(
    "datasets/campaigns.csv",
    index=False
)

# ==========================================
# AI VISIBILITY
# ==========================================

platforms = [

    "ChatGPT",

    "Gemini",

    "Claude",

    "Perplexity"

]

brands = [

    "AMEX",

    "Chase",

    "Capital One",

    "Citi"

]

prompts = [

    "best travel credit card",

    "best cashback card",

    "best business card",

    "best premium card"

]

visibility_df = pd.DataFrame({

    "Date":

        [

            start_date +
            timedelta(
                days=np.random.randint(
                    0,
                    730
                )
            )

            for _
            in range(
                N_VISIBILITY
            )

        ],

    "Platform":

        np.random.choice(
            platforms,
            N_VISIBILITY
        ),

    "Prompt":

        np.random.choice(
            prompts,
            N_VISIBILITY
        ),

    "Brand":

        np.random.choice(
            brands,
            N_VISIBILITY
        ),

    "Mentioned":

        np.random.choice(
            [0,1],
            N_VISIBILITY,
            p=[0.2,0.8]
        ),

    "Position":

        np.random.randint(
            1,
            6,
            N_VISIBILITY
        ),

    "Sentiment":

        np.random.choice(
            [
                "Positive",
                "Neutral",
                "Negative"
            ],
            N_VISIBILITY
        )

})

visibility_df.to_csv(
    "datasets/ai_visibility.csv",
    index=False
)

# ==========================================
# EXPERIMENTS
# ==========================================

experiment_df = pd.DataFrame({

    "Experiment_ID":

        np.repeat(
            range(
                1,
                N_EXPERIMENTS + 1
            ),
            2
        ),

    "Campaign":

        np.random.choice(
            campaign_names,
            N_EXPERIMENTS * 2
        ),

    "Variant":

        np.tile(
            ["A","B"],
            N_EXPERIMENTS
        ),

    "Visitors":

        np.random.randint(
            1000,
            20000,
            N_EXPERIMENTS * 2
        ),

    "Conversions":

        np.random.randint(
            50,
            2000,
            N_EXPERIMENTS * 2
        )

})

experiment_df.to_csv(
    "datasets/experiments.csv",
    index=False
)

print(
    "\nDatasets Generated Successfully\n"
)

print(
    search_df.shape,
    campaign_df.shape,
    visibility_df.shape,
    experiment_df.shape
)

# ==========================================
# CHANNEL PATHS
# ==========================================

N_CHANNEL_PATHS = 3000

channels = [
    "Paid Search",
    "Organic Search",
    "Email",
    "Display",
    "Social",
    "Affiliate"
]

channel_df = pd.DataFrame({

    "Customer_ID":

        range(
            1,
            N_CHANNEL_PATHS + 1
        ),

    "Channel":

        np.random.choice(
            channels,
            N_CHANNEL_PATHS
        ),

    "Revenue":

        np.random.uniform(
            100,
            10000,
            N_CHANNEL_PATHS
        ).round(2),

    "Conversions":

        np.random.randint(
            1,
            20,
            N_CHANNEL_PATHS
        )

})

channel_df.to_csv(
    "datasets/channel_paths.csv",
    index=False
)