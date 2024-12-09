FROM ubuntu:latest

# Install cron
RUN apt-get update && apt-get -y install cron

# Copy your cron job script
COPY mycronjob.sh /etc/cron.d/mycronjob.sh

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/mycronjob.sh

# Apply cron job
RUN crontab /etc/cron.d/mycronjob.sh

# Start cron service
CMD ["cron", "-f"]
