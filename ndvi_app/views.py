from django.shortcuts import render
from django.http import HttpResponse
from .forms import PathForm
import os
import rasterio

import rasterio
import numpy as np

def calculate_ndvi(band4_path, band5_path, output_path):
    try:
        # Open Band 4 and Band 5 datasets
        with rasterio.open(band4_path) as band4, rasterio.open(band5_path) as band5:
            b4 = band4.read(1).astype('float64')
            print(f"Band 4 Data: {b4}")

            b5 = band5.read(1).astype('float64')
            print(f"Band 5 Data: {b5}")

            # Using list comprehension and basic Python operations for NDVI calculation
            ndvi = [
                [
                    (b5_val - b4_val) / (b5_val + b4_val) if (b5_val + b4_val) != 0 else 0
                    for b5_val, b4_val in zip(b5_row, b4_row)
                ]
                for b5_row, b4_row in zip(b5, b4)
            ]

            profile = band4.profile
            print(profile)
            profile.update(dtype=rasterio.float64, count=1)

            with rasterio.open(output_path, 'w', **profile) as dst:
                dst.write(np.array(ndvi), 1)

        return True
    except Exception as e:
        print(f"Error calculating NDVI for {band4_path} and {band5_path}: {e}")
        return False

def process_year_directory(year_dir, output_dir):
    ndvi_generated = False
    
    for root, _, files in os.walk(year_dir):
        band4_path = None
        band5_path = None
        for file in files:
            if file.lower().endswith('b4.tif'):
                band4_path = os.path.join(root, file)
            elif file.lower().endswith('b5.tif'):
                band5_path = os.path.join(root, file)
        
        if band4_path and band5_path:
            print(f"Calculating NDVI for {band4_path} and {band5_path}")
            year_name = os.path.basename(year_dir)
            output_path = os.path.join(output_dir, f'ndvi_{year_name}.tif')
            if calculate_ndvi(band4_path, band5_path, output_path):
                ndvi_generated = True
            else:
                print(f"Failed to calculate NDVI for {band4_path} and {band5_path}")
        else:
            print(f"Missing band4.tif or band5.tif in {root}")
    
    return ndvi_generated

def ndvi_view(request):
    if request.method == 'POST':
        form = PathForm(request.POST)
        if form.is_valid():
            source_path = form.cleaned_data['source_path']
            destination_path = form.cleaned_data['destination_path']

            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            ndvi_generated = False
            for item in os.listdir(source_path):
                year_dir = os.path.join(source_path, item)
                if os.path.isdir(year_dir):
                    if process_year_directory(year_dir, destination_path):
                        ndvi_generated = True
            
            if ndvi_generated:
                return HttpResponse("NDVI files generated successfully.")
            else:
                return HttpResponse("No NDVI files generated. Please check the source directory contents.")
    else:
        form = PathForm()
    
    return render(request, 'ndvi_app/ndvi_form.html', {'form': form})
