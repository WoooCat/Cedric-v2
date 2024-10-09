DOCKER_COMPOSE_FILE = docker-compose.yml
DOCKER_COMPOSE_CMD = docker-compose -f $(DOCKER_COMPOSE_FILE)

# Commands for linting and formatting
FLAKE8_CMD = flake8 src
ISORT_CMD = isort src
BLACK_CMD = black src

help:
	@echo "Available commands:"
	@echo "  make start   - Start the application and database"
	@echo "  make stop    - Stop the application and database"
	@echo "  make clear  - Remove all stopped containers and volumes"
	@echo "  make status  - Check the status of the application and database"
	@echo "  make logs    - View logs of the services in real-time"

	@echo "  make lint    - Run flake8 to lint the code"
	@echo "  make sort    - Run isort to sort imports"
	@echo "  make format  - Run black to format code"
	@echo "  make check   - Run lint and format commands"


# Start Application and Database
start:
	$(DOCKER_COMPOSE_CMD) up --build -d

# Stop Application and Database
stop:
	$(DOCKER_COMPOSE_CMD) down

# Remove all stopped containers and volumes
clear:
	$(DOCKER_COMPOSE_CMD) down --volumes --rmi all

# Check status of Application and Database
status:
	$(DOCKER_COMPOSE_CMD) ps -a

# View logs of Services in real-time
logs:
	$(DOCKER_COMPOSE_CMD) logs -f



# LINTER AND FORMATTER COMMANDS
# Run flake8 to lint the code
lint:
	$(FLAKE8_CMD)

# Run isort to sort imports
isort:
	$(ISORT_CMD)

# Run black to format code
format:
	$(BLACK_CMD)

# Run lint, sort, and format commands
check: isort lint format