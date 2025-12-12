from hub import port
import runloop
import motor_pair
import motor


vel = 180
vel2 = 720

startingAttachmentAngle = 70

async def main():

    # Bring attachment to starting position
    await motor.run_to_absolute_position(port.D, startingAttachmentAngle, vel)

    # Move left
    await motor.run_for_degrees(port.E, 200, vel)

    # Move right
    await motor.run_for_degrees(port.A, -220, vel)


    # Pair motors
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

    # # Move forward
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 680, 0, velocity=vel)


    # Make a right turn
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 130, 100, velocity=vel2)

    # Make left turn
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 100, -100, velocity=vel2)

    # Return
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -800, 0, velocity=vel)
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())