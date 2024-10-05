# Function to calculate percentage change
def calculate_percentage_change(old_value, new_value):
    if old_value == 0:
        return 0  # Avoid division by zero
    return ((new_value - old_value) / old_value) * 100

# Function to analyze if the new video performed 1% better in key metrics
def analyze_video_performance(last_video_metrics, new_video_metrics):
    performance_improved = True
    key_metrics = ['views', 'likes', 'comments', 'shares', 'watch_time']

    for metric in key_metrics:
        if metric in last_video_metrics and metric in new_video_metrics:
            percentage_change = calculate_percentage_change(last_video_metrics[metric], new_video_metrics[metric])
            print(f"{metric.capitalize()} changed by {percentage_change:.2f}%")
            
            if percentage_change < 1:  # Check if the performance increased by at least 1%
                performance_improved = False

    if performance_improved:
        print("The new video performed at least 1% better across all metrics!")
    else:
        print("The new video did not perform 1% better in some metrics.")

# Example video performance data (last video vs new video)
last_video_metrics = {
    'views': 10000,
    'likes': 500,
    'comments': 100,
    'shares': 50,
    'watch_time': 20000  # in seconds
}

new_video_metrics = {
    'views': 10150,  # 1.5% increase
    'likes': 505,    # 1% increase
    'comments': 100, # No increase
    'shares': 51,    # 2% increase
    'watch_time': 20250  # 1.25% increase
}

# Run the analysis
analyze_video_performance(last_video_metrics, new_video_metrics)
