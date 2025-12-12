from hub import port
import runloop
import motor_pair
import motor

normalSpeed = 90
fastSpeed = 720
attachmentStartingPosition = 230

async def main():

    # Bring attachment to starting position
    await motor.run_to_absolute_position(port.D, attachmentStartingPosition, normalSpeed)

    # Make a right turn
    await motor.run_for_degrees(port.A, -90, 180)

    # Pair motors
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 410, 0, velocity=180)
    motor_pair.stop(motor_pair.PAIR_1)

    # Make a left turn
    await motor.run_for_degrees(port.A, 100, 180)

    # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 80, 0, velocity=180)
    motor_pair.stop(motor_pair.PAIR_1)

    # Move the attachment
    for i in range(5):
        await motor.run_to_absolute_position(port.D, attachmentStartingPosition - 80, fastSpeed)
        await motor.run_to_absolute_position(port.D, attachmentStartingPosition, fastSpeed)

    # Move backward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -250, 0, velocity=normalSpeed)
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())