import traceback

from tortoise import Tortoise

async def init_db():

    try:
        tortoise_config = {
            "connections":
            {
                "default":"postgres://mi7_postgresql_user:hK3YQNsEjpgaEyQTgTDshLYvwZ21ALDe@dpg-d11eanre5dus738m3i80-a.oregon-postgres.render.com/mi7_postgresql_db_name"
            },
            "apps":
            {
                "models":
                {
                    "models": ["models.orm_models.poc_employee",
                               "models.orm_models.poc_department"],
                    "default_connection":"default"
                }
            },
            "use_tz": False,
            "connections_params":{
                "default":
                {
                    "max_connections":10,
                    "min_conections":10,
                    "max_inactive_connections_lifetime":1
                }
            }
        }

        await Tortoise.init(config=tortoise_config)
        return True

    except Exception as e:
        traceback.print_exc()