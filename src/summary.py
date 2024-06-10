import pandas as pd

def create_summary_table(identified_viruses, metrics):
    data = []
    for virus, kmers in identified_viruses.items():
        # Assuming the virus format is "Virus Name Strain/Isolate | Accession Number"
        parts = virus.split('|')
        if len(parts) >= 2:
            name_isolate = parts[0].strip()
            accession_number = parts[1].strip()
            
            # Further split the name_isolate part into Virus Name and Strain/Isolate
            last_space_index = name_isolate.rfind(' ')
            virus_name = name_isolate[:last_space_index].strip()
            strain_isolate = name_isolate[last_space_index + 1:].strip()
        else:
            virus_name = virus
            strain_isolate = "N/A"
            accession_number = "N/A"
        
        data.append({
            "Virus Name": virus_name,
            "Strain/Isolate": strain_isolate,
            "Accession Number": accession_number,
            "Proportion (%)": (len(kmers) / sum(len(k) for k in identified_viruses.values())) * 100
        })
    
    df = pd.DataFrame(data)

    # Add metrics to the summary table
    metrics_data = {
        "Virus Name": ["Overall Metrics"],
        "Strain/Isolate": [""],
        "Accession Number": [""],
        "Proportion (%)": [""],
        "Shannon Diversity Index": [metrics['shannon_index']],
        "Simpson Diversity Index": [metrics['simpson_index']],
        "Richness": [metrics['richness']],
        "Evenness": [metrics['evenness']]
    }
    metrics_df = pd.DataFrame(metrics_data)

    # Concatenate the metrics row with the main data frame
    summary_df = pd.concat([df, metrics_df], ignore_index=True, sort=False)

    return summary_df
