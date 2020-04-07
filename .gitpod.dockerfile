FROM gitpod/workspace-full:latest

USER root
# Setup Heroku CLI
RUN curl https://cli-assets.heroku.com/install.sh | sh

USER gitpod
# Local environment variables
# C9_* variables are temporary
ENV C9_USER="gitpod"
ENV PORT="8080"
ENV IP="0.0.0.0"
ENV C9_HOSTNAME="localhost"

USER root
# Switch back to root to allow IDE to load
