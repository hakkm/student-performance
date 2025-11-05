
FROM jupyter/base-notebook:latest

# Install any extra packages you need
RUN pip install numpy pandas matplotlib scikit-learn