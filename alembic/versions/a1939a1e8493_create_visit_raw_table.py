"""Create visit raw table

Revision ID: a1939a1e8493
Revises: 
Create Date: 2019-03-13 23:03:17.988661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1939a1e8493'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('visits_raw',
                    sa.Column('item', sa.INT),
                    sa.Column('fecha', sa.VARCHAR(16)),
                    sa.Column('visitante', sa.VARCHAR(200)),
                    sa.Column('documento', sa.VARCHAR(50)),
                    sa.Column('entidad', sa.VARCHAR(100)),
                    sa.Column('motivo', sa.VARCHAR(200)),
                    sa.Column('empleado_publico', sa.VARCHAR(200)),
                    sa.Column('oficina', sa.VARCHAR(100)),
                    sa.Column('hora_ingreso', sa.VARCHAR(16)),
                    sa.Column('hora_salida', sa.VARCHAR(16)),
                    sa.Column('local', sa.VARCHAR(100))
                    )

def downgrade():
    op.execute('DROP SCHEMA drt CASCADE;')
