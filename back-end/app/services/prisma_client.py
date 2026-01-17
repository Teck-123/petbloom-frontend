from prisma import Prisma

class PrismaClient:
    _instance = None
    _prisma = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    async def connect(self):
        if self._prisma is None:
            self._prisma = Prisma()
            await self._prisma.connect()
        return self._prisma

    async def disconnect(self):
        if self._prisma:
            await self._prisma.disconnect()
            self._prisma = None

    def get_client(self):
        if self._prisma is None:
            raise RuntimeError("Prisma client not initialized. Call connect() first.")
        return self._prisma

prisma_client = PrismaClient()
