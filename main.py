from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import moderna

app = FastAPI(
    title="Web Scraping",
    description="Web Scraping",
    version="1.0.0"
)

# O asterisco referência que qualquer IP de máquina pode conectar nesse endereço da API que esteja dentro da rede
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # Liberar os métodos criados para que qualquer ip consiga utiliza-los
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(moderna.router)
